#!/usr/bin/env python3

import requests

class FictionJunction(object):
    __url_login = 'http://www.fictionjunction.org/logging.php?action=login'

    def __init__(self):
        self.r = requests.Session()

    def login(self):
        res = self.r.get(self.__url_login)

    def start(self):
        self.login()

if '__main__' == __name__:
    fj = FictionJunction()
    fj.start()
