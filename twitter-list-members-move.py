#!/usr/bin/env python3

import configparser
import os
import sys
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

    cnt = int(sys.argv[5])
    user1 = sys.argv[1]
    list1 = sys.argv[2]
    user2 = sys.argv[3]
    list2 = sys.argv[4]

    users = t.GetListMembers(slug=list1, owner_screen_name=user1)
    for i in range(0, cnt):
        try:
            user = users[i]
            print('Processing {} now...'.format(user.screen_name))

            print('Delete {} from {} now...'.format(user.screen_name, list1))
            t.DestroyListsMember(slug=list1, owner_screen_name=user1, screen_name=user.screen_name)

            print('Add {} to {} now...'.format(user.screen_name, list2))
            t.CreateListsMember(slug=list2, owner_screen_name=user2, screen_name=user.screen_name)

        except twitter.error.TwitterError as e:
            print('Got error {}'.format(e.message))

if '__main__' == __name__:
    work()
