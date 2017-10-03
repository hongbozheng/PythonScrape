import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import requests
from bs4 import BeautifulSoup
import re
import json
# from bs4 import beautifulsoup4
#requests.packages.urllib3.disable_warnings()


with requests.Session() as c:


    LOGIN_URL="https://www.ourtime.com/v3/login/process"
    # URL="http://www.ourtime.com/v3/search/results?start=1&sortCol=MyDefault&DisplayResultsStyle=true"
    URL="http://www.ourtime.com/v3/profile?profile=E3DBD410C354ED6CACA0C235BB8ED21D&search=true&start=1&sortby=0"
    # URL = "http://www.ourtime.com//v3/profile?profile=930C461F7082293CACA0C235BB8ED21D&search=true&start=1&sortby=0"

    html = c.get(LOGIN_URL)
    soup = BeautifulSoup(html.content,'html.parser')
    payload = {
        "username": "rainzheng258@gmail.com",
        "password": "zheng123456",
        "FromLocation":"/v3/logout",
        "chkKeepMeLoggedIn":"true"
    }
    p = c.post(LOGIN_URL,data=payload)
    print p




    page = c.get(URL).content
    pic_urls = re.findall('"PhotoUrl":"(.*?)",', page, re.S)

    for pic in pic_urls:
      print "--------------"
      print pic



         # photos = json.loads(pic_urls)
    # print photos
    # soupPage = BeautifulSoup(page.content,'html.parser')
    # print soupPage
    # divs = soupPage.find('img',{"id":"FullPhotoImage"})
    # divs = soupPage.findAll('script',{"type":"text/javascript"})
    # for div in divs:
    #  print "------------------------"
    #  print div




