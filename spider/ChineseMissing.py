
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import itertools

import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import requests
import os
import urllib
from datetime import datetime as dt

def count(start=0, step=1):
    n = start
    i = 0
    while i<40:
        yield n
        n += step
        i +=1

def getUrls():
    # url = r"http://www.zgszrkdak.cn/home/bdrq/roamerlist/p/{pn}.html"
    url=r"http://www.zgszrkdak.com/list.asp?id=2&PageNo={pn}"
    urls = (url.format(pn=x) for x in count(start=1, step=1))
    return urls


dirpath = '/Users/danny/PycharmProjects/spider/' + 'chinesem'


urls = getUrls()
index = 6038
start_time = dt.now()
for url in urls:
      print 'url: ' + str(url)

      html = requests.get(url).text
      # pic_urls = re.findall('"objURL":"(.*?)",',html,re.S)#baidu image

      # pic_urls = re.findall('<img src="/Public/upfiles(.*?)" ',html,re.S)
      pic_urls = re.findall('<img src="upfiles(.*?)" ', html, re.S)
      if not os.path.isdir(dirpath):
            os.mkdir(dirpath)

      print  'total images: ' + str(len(pic_urls))

      for pic_url in pic_urls:
         # pic_url = "http://www.zgszrkdak.cn/Public/upfiles" + pic_url
         # "http://www.zgszrkdak.com/upfiles/201707/20170728104024480.jpg"
         pic_url = "http://www.zgszrkdak.com/upfiles" + pic_url
         print 'Downloading: ' + str(index + 1) + ' image, address:' + str(pic_url)

         try:
           res = requests.get(pic_url,timeout=10)
           if str(res.status_code)[0] == "4":
              print("Fail download: ",pic_url)
              continue
         except Exception as inst:
           print("Fail download2: ", pic_url)
           print(type(inst))  # the exception instance
           print(inst.args)  # arguments stored in .args
           print(inst)
         filename = os.path.join(dirpath,str(index) + ".jpg")
         with open(filename,'wb') as f:
            f.write(res.content)
            index += 1
print("Finish download %s images" % index)
print "time used :", dt.now() - start_time


