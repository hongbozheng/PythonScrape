import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import requests
from bs4 import BeautifulSoup
import re

with requests.Session() as c:


    LOGIN_URL="https://www.ourtime.com/v3/login/process"
    URL="http://www.ourtime.com/v3/search/results?start=1&sortCol=MyDefault&DisplayResultsStyle=true"
  # "https://www.blackpeoplemeet.com/v3/login/process"
  # "https://www.blackpeoplemeet.com/v3/search/results?start=2&sortcol=MyDefault"
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

    searchURL = "http://www.ourtime.com/v3/search/processlegacyasync"
    searchpayload = {
         "ShowZip":"false",
         "ZipCode":"" ,
        "Location":"US-FL",
        "MinAge":20,
         "MaxAge":40,
         "MinHeight":48,
         "MaxHeight":95,
         "LookingFor":-1,
         "Status":-1,
         "Smoking":-1,
         "BodyType":-1,
         "HasPhotos":1,
         "Ethnicity":-1,
         "Religion":-1,
         "Zodiac":-1,
         "Children":-1,
         "DisplayGallery":"true",
         "Sortby":"MyDefault",
    }

    c.post(searchURL,data=searchpayload)

    page = c.get(URL)
    soupPage = BeautifulSoup(page.content,'html.parser')
    #print soupPage
    divs = soupPage.findAll('div',{"class":"results-item"})
    # print divs
    print len(divs)
    for div in divs:
        print '------------------'
        print div
        # a = div.find('a')
        # profileurl = 'http://www.ourtime.com/' + a['href']
        # name = a.string

        # print name
        # print profileurl
        # page = c.get(URL).content
        # pic_urls = re.findall('"PhotoUrl":"(.*?)",', page, re.S)
        # print "photos: ", len(pic_urls)
        # for pic in pic_urls:
        #     print pic



