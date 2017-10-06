import tweepy

CONSUMER_KEY = "NOu7CgBemfXGAcEI2ksikd94U"
CONSUMER_SECRET = "3y4kJmvmVbpMR5KdVxwCfxNxD9e3SHlmhVtra617yx2mCxErPj" 
ACCESS_KEY = "915043531118362624-W4buHVKSXlvSSXjtVK78qJbPwwvqK1Q"
ACCESS_SECRET = "fQyum8Zpu3hyT5shkaNtvcplYv00ZAdPIxpuiG2FrbuHF" 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
