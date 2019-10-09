#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from src.cloudflare_worker import CloudflareWorker

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--domain', action='store', dest='domain', help='Cloudflare fqdn domain name', required=True)
parser.add_argument('-r', '--route', action='store', dest='route', help='Cloudflare worker route pattern', required=True)
parser.add_argument('-s', '--script', action='store', dest='script', default=None, help='Script to use on the route', required=False)

args = parser.parse_args()

def main():
    cf = CloudflareWorker(args.domain)
    success = cf.update_route(args.route, script=args.script)
    if success:
        print('Cloudflare script %s have been enabled on %s in %s' %(args.script, args.route, args.domain))

if __name__ == "__main__":
    main()
