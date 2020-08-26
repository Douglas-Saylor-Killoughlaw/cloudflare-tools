#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
from src.cloudflare_tools import CloudflareTools

parser = argparse.ArgumentParser()

parser.add_argument('-d', '--domain', action='store', dest='domain', help='Cloudflare fqdn domain name', required=True)
parser.add_argument('-n', '--name', action='store', dest='name', help='Cloudflare access app name', required=True)
parser.add_argument('-u', '--url', action='store', dest='url', help='Cloudflare access app URL', required=True)

args = parser.parse_args()

def main():
    cf = CloudflareTools(args.domain)
    success = cf.set_access_url(args.name, args.url)
    if success:
        print('Cloudflare Access App for %s has been set to %s on %s' %(args.name, args.url, args.domain))

if __name__ == "__main__":
    main()
