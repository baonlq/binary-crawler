#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from splinter import Browser

from constant import login_url, email, password, trading_url, r_length

executable_path = {'executable_path': 'phantomjs/bin/phantomjs.exe'}
browser = Browser('phantomjs', **executable_path)
# browser = Browser('chrome')


def tracking():
    i = 0
    r = []
    browser.visit(trading_url)
    time.sleep(5)
    while True:
        if i == r_length:
            with open('crawled/data.csv', 'a') as file:
                file.write('{}\n'.format(','.join(r)))
                r = []
                i = 0

        el = browser.find_by_xpath('//*[@id="spot"]')
        print '[{}] {}'.format(time.strftime("%d/%m/%Y %H:%M:%S"), el.text)
        r.append(el.text)
        i += 1
        time.sleep(10)


try:
    browser.visit(login_url)
    browser.fill('email', email)
    browser.fill('password', password)
    browser.find_by_name('login').click()
    tracking()
except Exception as e:
    print e
