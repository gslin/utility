#!/usr/bin/env python3

import mechanicalsoup
import os
import requests
import sys

def archive_archive_fo(url):
    b = mechanicalsoup.StatefulBrowser()
    b.open('https://archive.fo/')

    print('* Opened')

    b.select_form('#submiturl')
    b['url'] = url
    b.submit_selected()

    print('* Submitted')

    b.close()

def archive_web_archive_org(url):
    url = 'https://web.archive.org/save/' + url
    res = requests.get(url)

    print('* Submitted')

def main():
    os.environ['all_proxy'] = 'socks5://127.0.0.1:9050'

    url = sys.argv[1]

#    print('* Calling web.archive.org: {}'.format(url))
#    archive_web_archive_org(url)

    print('* Calling archive.fo: {}'.format(url))
    archive_archive_fo(url)

if '__main__' == __name__:
    main()
