import urllib2,urllib
from urllib import urlencode
import re,sys,os,time,Queue,thread,cookielib

# url = 'http://search.jiayuan.com/v2/index.php'
url = 'http://search.jiayuan.com/v2/index.php?key=&sex=f&stc=1:51,2:18.21,3:158.170,23:1,4:30.0&sn=default&sv=1&pt=236&ft=off&f=select&mt=d'

uid = '133574961'
passwd = 'lixiaoming'
values = {'password':passwd,'name':uid,'validate_code':'','_s_x_id':'_s_x_id:d7af9140cbeb24358c8f190ab6e4f14c'}
postdata = urllib.urlencode(values)

cookie = cookielib.CookieJar()
urlopener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie),urllib2.HTTPHandler)

headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36',
         'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
         }

req = urllib2.Request(
    # url = 'http://passport.jiayuan.com/dologin.php',
    url = 'https://passport.jiayuan.com/dologin.php?pre_url=http://www.jiayuan.com',
    data = postdata,
    headers = headers
)

urlopener.open(req)
page = urlopener.open(url).read()

print  page
unicodePage = page.decode("utf-8")

#print unicodePage
rst = re.compile('<div class="user_name">(.*?)</div>',re.S)
items = rst.findall(unicodePage)
print items
for item in items:
   print item[0],item[1]
