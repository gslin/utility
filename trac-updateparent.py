#!/usr/bin/env python3

import configparser
import datetime
import getopt
import os
import sys
import time
import xmlrpc.client

class TracUpdateTicketBot(object):
    def __init__(self):
        home = os.environ['HOME']
        f_conf = '{}/.config/tracbot/config.ini'.format(home)

        c = configparser.ConfigParser()
        c.read(f_conf)

        uri = c['default']['uri']
        self.s = xmlrpc.client.ServerProxy(uri)

    def start(self):
        opts, args = getopt.getopt(
            sys.argv[1:],
            '',
            ['parents='],
        )

        a = {}

        for opt, arg in opts:
            if '--parents' == opt:
                a['parents'] = arg

        for id_str in args:
            id = int(id_str)
            print('* Updating {}'.format(id))
            self.s.ticket.update(id, '', a, True)

if '__main__' == __name__:
    t = TracUpdateTicketBot()
    t.start()
