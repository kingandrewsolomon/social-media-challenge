#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, sys

argfile = str(sys.argv[1])

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'NOu7CgBemfXGAcEI2ksikd94U'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '3y4kJmvmVbpMR5KdVxwCfxNxD9e3SHlmhVtra617yx2mCxErPj'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '915043531118362624-W4buHVKSXlvSSXjtVK78qJbPwwvqK1Q'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'fQyum8Zpu3hyT5shkaNtvcplYv00ZAdPIxpuiG2FrbuHF'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open(argfile,'r')
f=filename.readlines()
filename.close()

for line in f:
    api.update_status(line)
    time.sleep(900)#Tweet every 15 minutes
