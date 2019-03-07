#!/usr/bin/env python3

import mechanicalsoup
import os
import requests
import sys

def archive_web_archive_org(url):
    url = 'https://web.archive.org/save/' + url
    res = requests.get(url)

    print('* Submitted')

def main():
    url = sys.argv[1]

    print('* Calling web.archive.org: {}'.format(url))
    archive_web_archive_org(url)

if '__main__' == __name__:
    main()
