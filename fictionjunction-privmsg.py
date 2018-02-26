#!/usr/bin/env python3

import configparser
import lxml.html
import parse
import os
import requests

class FictionJunctionPrivmsg(object):
    __url_login = 'http://www.fictionjunction.org/logging.php?action=login'
    __url_login_post = 'http://www.fictionjunction.org/logging.php?action=login&loginsubmit=yes'
    __url_privmsg = 'http://www.fictionjunction.org/pm.php?filter=privatepm&page={}'
    __url_privmsg_template = 'http://www.fictionjunction.org/pm.php?uid={}&filter=privatepm&daterange=5'

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

            for entry in body.cssselect('a[href^="pm.php?uid="]'):
                href = entry.get('href')
                (uid, _) = parse.parse('pm.php?uid={}&{}', href)
                self.scrape_uid(uid)

            if not body.cssselect('.next'):
                break

            page += 1

    def scrape_uid(self, uid):
        page = 1

        url = self.__url_privmsg_template.format(uid)
        print('* Scraping webpage {}'.format(url))
        res = self.r.get(url)
        res.encoding = 'gbk'

        fname = 'fictionjunction.org-privmsg/{}.html'.format(uid)
        with open(fname, 'wb+') as f:
            f.write(res.content)

    def start(self):
        self.login()
        self.scrape()

if '__main__' == __name__:
    fj = FictionJunctionPrivmsg()
    fj.start()
