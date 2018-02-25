#!/usr/bin/env python3

import configparser
import lxml.html
import os
import requests

class FictionJunction(object):
    __url_login = 'http://www.fictionjunction.org/logging.php?action=login'
    __url_login_post = 'http://www.fictionjunction.org/logging.php?action=login&loginsubmit=yes'
    __url_thread_template = 'http://www.fictionjunction.org/viewthread.php?tid={}&page={}'

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
        for i in range(1, 8000):
            self.scrape_thread(i)

    def scrape_thread(self, n):
        page = 1

        # Hard-code protection.
        while page < 1000:
            url = self.__url_thread_template.format(n, page)
            print('* Scraping webpage {}'.format(url))
            res = self.r.get(url)
            res.encoding = 'gbk'

            if '指定的主题不存在或已被删除或正在被审核' in res.text:
                print('* Server return not found.')
                return

            if '下一页' not in res.text:
                return

            page += 1

    def start(self):
        self.login()
        self.scrape()

if '__main__' == __name__:
    fj = FictionJunction()
    fj.start()
