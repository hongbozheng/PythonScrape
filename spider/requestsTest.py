import sys
sys.path.append("/usr/local/lib/python2.7/site-packages")
import requests
from bs4 import BeautifulSoup
# from bs4 import beautifulsoup4
#requests.packages.urllib3.disable_warnings()


with requests.Session() as c:

    # LOGIN_URL ="https://www.eastmeeteast.com/login"
    # URL = "https://www.eastmeeteast.com/search?page=2"

    LOGIN_URL ="https://www.2redbeans.com/en/api/v2/user_sessions"
    URL = "https://www.2redbeans.com/en/app/search"

    # print payload
    html = c.get(LOGIN_URL)
    soup = BeautifulSoup(html.content,'html.parser')
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

    payload = {
        # "authenticity_token": authenticity_token,
        "user_session[email]": "bobzheng258@gmail.com",
        "user_session[password]": "zheng198916",
        # "commit": "Login"
    }

    # user_session[email] = bobzheng258 % 40
    # gmail.com & user_session[password] = zheng198916
    p = c.post(LOGIN_URL,data=payload)
    print p.content
    page = c.get(URL)
    soupPage = BeautifulSoup(page.content,'html.parser')
    # print soupPage
    imgs = soupPage.findAll('div',{"class":"search_result_img-container"})
    print len(imgs)
    for img in imgs:
        print img










# payload = {
#     'username':'sopier',
#     'password':'somepassword'
# }
# with requests.Session(config={'verbose':sys.stderr}) as c:
#      c.post('http://m.kaskus.co.id/user/login',data=payload)
#      r = c.get('http://m.kaskus.co.id/myforum')
#      print 'sopier' in r.content