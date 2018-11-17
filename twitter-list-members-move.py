#!/usr/bin/env python3

import configparser
import os
import twitter

def work():
    home = os.environ['HOME']
    f_conf = '{}/.config/twitter-list-members-move/config.ini'.format(home)

    c = configparser.ConfigParser()
    c.read(f_conf)

    t_ak = c['default']['twitter_access_token_key']
    t_as = c['default']['twitter_access_token_secret']
    t_ck = c['default']['twitter_consumer_key']
    t_cs = c['default']['twitter_consumer_secret']
    t = twitter.Api(access_token_key=t_ak, access_token_secret=t_as, consumer_key=t_ck, consumer_secret=t_cs)

if '__main__' == __name__:
    work()
