# Python Cloudflare Tools

`Cloudflare Tools` was written in order to easily enable/disable Cloudflare Worker/Access as required. I had several internal or test websites that are web protected by using Cloudflare Worker and Cloudflare Access. And this cause some issue when we were trying to run some page checks on this websites. So the purpose for this script is to disable the either Cloudflare Access/Worker before we will run the tests and re-enable it again when it's done as part of the jenkins pipeline. Currently it only supports several basic functions:
* Disable script from specific cloudflare worker route pattern
* Enable cloudflare worker on specific worker route pattern
* Set Cloudflare Access App URL based on the specified name


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
Cloudflare script basic-http-auth has been enabled in https://staging.mydomain.com/* on mydomain.com

$ python3.7 cf_access_app.py -d mydomain.com -n 'MyDomain Staging App' -u '_disabled.staging.mydomain.com/'
Cloudflare Access App for MyDomain Staging App has been set to _disabled.staging.mydomain.com/ on mydomain.com
```

## Note
This is written on python 3.7. So i haven't tested it yet on python <= 3.7. So use on your own risk and update as required.