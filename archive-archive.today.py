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

def main():
    url = sys.argv[1]

    print('* Calling archive.fo: {}'.format(url))
    archive_archive_fo(url)

if '__main__' == __name__:
    main()
