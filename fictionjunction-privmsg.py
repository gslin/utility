#!/usr/bin/env python3

import configparser
import lxml.html
import os
import requests

class FictionJunctionPrivmsg(object):
    __url_login = 'http://www.fictionjunction.org/logging.php?action=login'
    __url_login_post = 'http://www.fictionjunction.org/logging.php?action=login&loginsubmit=yes'

    def __init__(self):
        self.r = requests.Session()

        home = os.environ['HOME']
        f_conf = '{}/.config/fictionjunction.org/config.ini'.format(home)

        c = configparser.ConfigParser()
        c.read(f_conf)

        self.password = c['default']['password']
        self.username = c['default']['username']

    def login(self):
        res = self.r.get(self.__url_login)
        res.encoding = 'gbk'

        body = lxml.html.fromstring(res.text)

        formhash = body.cssselect('input[name="formhash"]')[0].value
        res = self.r.post(self.__url_login_post, data={
            'answer': '',
            'formhash': formhash,
            'loginfield': 'username',
            'loginsubmit': 'true',
            'password': self.password,
            'questionid': 0,
            'username': self.username,
        })
        res.encoding = 'gbk'

    def start(self):
        self.login()

if '__main__' == __name__:
    fj = FictionJunctionPrivmsg()
    fj.start()
