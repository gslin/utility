#!/usr/bin/env python3

import configparser
import lxml.html
import os
import requests

class FictionJunctionPrivmsg(object):
    __url_login = 'http://www.fictionjunction.org/logging.php?action=login'
    __url_login_post = 'http://www.fictionjunction.org/logging.php?action=login&loginsubmit=yes'
    __url_privmsg = 'http://www.fictionjunction.org/pm.php?filter=privatepm&page={}'

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

    def scrape(self):
        page = 1

        while True:
            url = self.__url_privmsg.format(page)

            print('* Scraping webpage {}'.format(url))
            res = self.r.get(url)
            res.encoding = 'gbk'

            body = lxml.html.fromstring(res.text)

            if not body.cssselect('.next'):
                break

            page += 1

    def start(self):
        self.login()
        self.scrape()

if '__main__' == __name__:
    fj = FictionJunctionPrivmsg()
    fj.start()
