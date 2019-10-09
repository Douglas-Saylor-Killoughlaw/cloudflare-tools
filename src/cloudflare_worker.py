#!/usr/bin/env python
"""Cloudflare Workers"""

import CloudFlare


class CloudflareWorker(object):
    def __init__(self, zone_name):
        self.cf = CloudFlare.CloudFlare()
        self.zone_name = zone_name

    def get_zone_detail(self):
        """function to get zone detail based on domain name"""
        try:
            params = {
                'name': self.zone_name,
                'per_page': 1
            }
        except IndexError:
            exit('Please input the domain name')

        try:
            zones = self.cf.zones.get(params=params)
            if zones == []:
                exit('Domain %s is not found in your account' %( self.zone_name ))
        except CloudFlare.exceptions.CloudFlareAPIError as e:
            exit('/zones %d %s - api call failed' % (e, e))
        except Exception as e:
            exit('/zones.get - %s - api call failed' % (e))

        for zone in sorted(zones, key=lambda v: v['name']):
            zone_name = zone['name']
            zone_id = zone['id']
            if 'email' in zone['owner']:
                zone_owner = zone['owner']['email']
            else:
                zone_owner = '"' + zone['owner']['name'] + '"'
            zone_plan = zone['plan']['name']

        return [zone_id, zone_name, zone_owner]

    def get_route_id(self, route_pattern):
        """get cloudflare route id based on given route pattern"""
        zone_id, zone_name, zone_owner = self.get_zone_detail()
        routes = self.cf.zones.workers.routes.get(zone_id)
        route_id = list(filter(lambda route: route['pattern'] == route_pattern, routes))[0]['id']
        return route_id

    def update_route(self, route_pattern, script=None):
        """ update cloudflare route for specific route pattern. Can be used to enable or disable route pattern """
        data = {
            'pattern': route_pattern,
            'script': script
        }

        try:
            zone_id, zone_name, zone_owner = self.get_zone_detail()
            route_id = self.get_route_id(route_pattern)
            result = self.cf.zones.workers.routes.put(zone_id, route_id, data=data)
            return True
        except CloudFlare.exceptions.CloudFlareAPIError as e:
            exit('/zones %d %s - api call failed' % (e, e))
        except Exception as e:
            exit('/zones.get - %s - api call failed' % (e))