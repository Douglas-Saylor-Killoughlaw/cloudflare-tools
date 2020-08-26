#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from src.cloudflare_tools import CloudflareTools

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--domain', action='store', dest='domain', help='Cloudflare fqdn domain name', required=True)
parser.add_argument('-r', '--route', action='store', dest='route', help='Cloudflare worker route pattern', required=True)
parser.add_argument('-s', '--script', action='store', dest='script', default=None, help='Script to use on the route', required=False)

args = parser.parse_args()

def main():
    cf = CloudflareTools(args.domain)
    success = cf.update_worker_route(args.route, script=args.script)
    if success:
        print('Cloudflare script %s has been enabled in %s on %s' %(args.script, args.route, args.domain))

if __name__ == "__main__":
    main()
