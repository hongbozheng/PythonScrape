import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import requests
from bs4 import BeautifulSoup
# from bs4 import beautifulsoup4
#requests.packages.urllib3.disable_warnings()


with requests.Session() as c:

    # LOGIN_URL ="https://www.eastmeeteast.com/login"
    # URL = "https://www.eastmeeteast.com/search?page=2"

    # LOGIN_URL ="https://www.asiandate.com/Pages/Security/Login.aspx?logout=1"
    # LOGIN_URL ="https://www.dateinasia.com/SignIn"
    # URL ="https://www.asiandating.com/fr/home/showMenu?login"
    # URL="http://www.asiandate.com/online-ladies2.html"
    # URL="https://www.dateinasia.com/Search.aspx?pg=0&g=1&af=18&at=99&c=JP"
    LOGIN_URL = "https://www.zoosk.com/v4.0/login/general_v42.php?format=json&product=1"
    URL="https://www.zoosk.com/personals/search?page=1&view=grid"
    html = c.get(URL)
    # print html.content
    soup = BeautifulSoup(html.content,'html.parser')
    print  soup
    # authenticity_token = soup.find('meta',{"name":"csrf-token"})['content']
    # print '**************',authenticity_token
    # payload = {
    #     "authenticity_token": authenticity_token,
    #     "user[email]": "dannyzhengtest2@gmail.com",
    #     "user[password]": "zheng123456",
    #     "user[remember_me]":"0",
    #     "user[remember_me]":"1",
    #     "commit": "Login"
    # }

    # payload = {
    #     # "authenticity_token": authenticity_token,
    #     "ctl00$ucContent$cntrlLogin$txtBoxLogin": "dannyzhengtest@gmail.com",
    #     "ctl00$ucContent$cntrlLogin$txtBoxPassword": "zheng123456",
    #     "ctl00$ucContent$cntrlLogin$btnLogin": "Login"
    # }

    payload = {
        "login": "dannyzhengtest@gmail.com",
        "password": "zheng123456",
        "from":"user-menu"
    }
    # user_session[email] = bobzheng258 % 40
    # gmail.com & user_session[password] = zheng198916
    p = c.post(LOGIN_URL,data=payload)
    print p
    # print p.content
    page = c.get(URL)
    soupPage = BeautifulSoup(page.content,'html.parser')
    print soupPage
    imgs = soupPage.findAll('li',{"class":"grid-tile"})
    print len(imgs)
    for img in imgs:
        print img['data-guid']


