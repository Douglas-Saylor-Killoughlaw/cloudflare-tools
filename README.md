# Python Cloudflare Worker Route

`Cloudflare Worker Route` was written in order to easily disable specific script from some route pattern on Cloudflare or to enable it back as required. I had several internal or test websites that are web protected by using Cloudflare using basic http auth. And this cause some issue when we were trying to run some page checks on this websites. So the purpose for this script is to disable the cloudflare worker before we will run the tests and enable it again when it's done as part of the jenkins pipeline

## Requirements
This script require Cloudflare module. Simply install it with
```shell
$ pip install cloudflare
```

## Quickstart

Set your cloudflare authentication in ~/.cloudflare/cloudflare.cfg
```
[CloudFlare]
email = alamsyah@mydomain.com
token = SomeRandomToken
```

Run the script with:
```shell
$ python3.7 cf_worker_route.py -d mydomain.com -r 'https://staging.mydomain.com/*' -s basic-http-auth
Cloudflare script basic-http-auth have been enabled on https://staging.mydomain.com/* in mydomain.com
```

## Note
This is written on python 3.7. So i haven't tested it yet on python <= 3.7. So use on your own risk and update as required.