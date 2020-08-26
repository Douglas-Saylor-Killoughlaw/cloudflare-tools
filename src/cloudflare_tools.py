#!/usr/bin/env python
"""Cloudflare Tools"""

import CloudFlare


class CloudflareTools(object):
    def __init__(self, zone_name):
        self.cf = CloudFlare.CloudFlare()
        self.zone_name = zone_name
        self.get_zone_detail()

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
            self.zone_name = zone['name']
            self.zone_id = zone['id']
            if 'email' in zone['owner']:
                self.zone_owner = zone['owner']['email']
            else:
                self.zone_owner = '"' + zone['owner']['name'] + '"'
            zone_plan = zone['plan']['name']

    def get_worker_route_id(self, route_pattern):
        """get cloudflare route id based on given route pattern"""
        routes = self.cf.zones.workers.routes.get(self.zone_id)
        route_id = list(filter(lambda route: route['pattern'] == route_pattern, routes))[0]['id']
        return route_id

    def update_worker_route(self, route_pattern, script=None):
        """ update cloudflare route for specific route pattern. Can be used to enable or disable route pattern """
        data = {
            'pattern': route_pattern,
            'script': script
        }

        try:
            route_id = self.get_worker_route_id(route_pattern)
            result = self.cf.zones.workers.routes.put(self.zone_id, route_id, data=data)
            return True
        except CloudFlare.exceptions.CloudFlareAPIError as e:
            exit('/zones.workers.routes %d %s - api call failed' % (e, e))
        except Exception as e:
            exit('/zones.workers.routes.put - %s - api call failed' % (e))

    def get_access_app_id(self, app_name):
        """get cloudflare access app id based on given app name"""
        apps = self.cf.zones.access.apps.get(self.zone_id)
        app_id = list(filter(lambda app: app['name'] == app_name, apps))[0]['id']
        return app_id

    def set_access_url(self, app_name, url):
        """ update cloudflare access url. Can be used to set the url based on the given app_name"""
        data = {
            'name': app_name,
            'domain': url
        }

        try:
            app_id = self.get_access_app_id(app_name)
            result = self.cf.zones.access.apps.put(self.zone_id, app_id, data=data)
            return True
        except CloudFlare.exceptions.CloudFlareAPIError as e:
            exit('/zones.access.apps %d %s - api call failed' % (e, e))
        except Exception as e:
            exit('/zones.access.apps.put - %s - api call failed' % (e))