#!/usr/bin/env python3

import lxml.html
import requests

class FictionJunction(object):
    __url_login = 'http://www.fictionjunction.org/logging.php?action=login'

    def __init__(self):
        self.r = requests.Session()

    def login(self):
        res = self.r.get(self.__url_login)
        body = lxml.html.fromstring(res.text)

        formhash = body.cssselect('input[name="formhash"]')[0].value

    def start(self):
        self.login()

if '__main__' == __name__:
    fj = FictionJunction()
    fj.start()
