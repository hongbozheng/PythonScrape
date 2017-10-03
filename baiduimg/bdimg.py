# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import itertools

import sys

sys.path.append("/usr/local/lib/python2.7/site-packages")
import requests
import os
from datetime import datetime as dt


def count(start=0, step=1):
    n = start
    i = 0
    pages = 97
    while i <= pages*20/60:
        yield n
        n += step
        i += 1


def getUrls():
    # url=r"http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E7%94%B7%E6%98%8E%E6%98%9F%E5%9B%BE%E7%89%87%E5%A4%A7%E5%85%A8&pn={pn}"
    # url = r"http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E6%98%8E%E6%98%9F%E5%A4%B4%E5%83%8F&pn={pn}&gsm=50"
    # url = r"https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E8%AF%81%E4%BB%B6%E7%85%A7&pn={pn}"
    url = r"http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=证件照男&pn={pn}"
    urls = (url.format(pn=x) for x in count(start=0, step=60))
    return urls


dirpath = '/Users/danny/PycharmProjects/spider/' + 'IDpicmale'

urls = getUrls()
index = 1
start_time = dt.now()
for url in urls:
    print 'url: ' + str(url)

    html = requests.get(url).text
    pic_urls = re.findall('"objURL":"(.*?)",',html,re.S)#baidu image

    if not os.path.isdir(dirpath):
        os.mkdir(dirpath)

    print  'total images: ' + str(len(pic_urls))

    for pic_url in pic_urls:
        print 'Downloading: ' + str(index + 1) + ' image, address:' + str(pic_url)

        try:
            res = requests.get(pic_url, timeout=10)
            if str(res.status_code)[0] == "4":
                print("Fail download: ", pic_url)
                continue
        except Exception as inst:
            print("Fail download2: ", pic_url)
            print(type(inst))  # the exception instance
            print(inst.args)  # arguments stored in .args
            print(inst)
        filename = os.path.join(dirpath, str(index) + ".jpg")
        with open(filename, 'wb') as f:
            f.write(res.content)
            index += 1
print("Finish download %s images" % index)
print "time used :", dt.now() - start_time


