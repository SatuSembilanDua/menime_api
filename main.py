import flask
from flask import request, jsonify, json
from bs4 import BeautifulSoup
import cfscrape
import html
import base64
import cloudscraper

def e_url(s):
    ssb = s.encode("ascii") 

    base64_bytes = base64.b64encode(ssb) 
    base64_string = base64_bytes.decode("ascii") 
    
    strstr = base64_string.translate(str.maketrans('+/', '-_'))
    return strstr.rstrip('=') 

def d_url(s):
    strstr = s.translate(str.maketrans('+/', '-_'))
    le = len(s) + 10
    pad_right = strstr.ljust(le, '=')
    ret = base64.b64decode(pad_right).decode('utf-8')
    return ret

def anifo(URL):
    URL = d_url(URL)
    #URL = 'https://www.oploverz.in/series/one-piece-sub-indo/'
    # scraper = cfscrape.create_scraper()
    scraper = cloudscraper.create_scraper()
    soup = BeautifulSoup(scraper.get(URL).content, 'html.parser')

    desc = soup.find('span', class_='desc')
    listinfo = soup.find('div', class_='listinfo')
    img_des = soup.find('div', class_='imgdesc')
    img = img_des.findChildren("img" , recursive=False)

    a = desc.prettify(formatter="html5")
    b = listinfo.prettify(formatter="html5")
    c = a.replace('"', "\"")
    d = b.replace('"', "\"")
    e = html.escape(c)
    f = html.escape(d)
    ret = {'desc':e,'info':f,'img':img[0]["src"]}
    jsona = json.dumps(ret)
    return jsona

def get_vid(URL):
    URL = d_url(URL)
    # scraper = cfscrape.create_scraper()
    scraper = cloudscraper.create_scraper()
    soup = BeautifulSoup(scraper.get(URL).content, 'html.parser')
    
    iframe = soup.find('iframe', class_='idframe')
    #a = iframe.prettify(formatter="html5")
    # e = html.escape(a)
    return iframe['src']

def get_eps_list(URL):
    URL = d_url(URL)
    scraper = cloudscraper.create_scraper()
    soup = BeautifulSoup(scraper.get(URL).content, 'html.parser')

    episodelist = soup.find(class_='episodelist')
    ret = []
    for li in episodelist.find_all("li"):
        eps = li.find(class_="leftoff")
        judul = li.find(class_="lefttitle")
        dt = li.find(class_="rightoff")
        alink = eps.find("a")
        con = {
                'link':alink.get('href'),
                'eps':eps.get_text().strip(),
                'judul':judul.get_text().strip(),
                'date':dt.get_text().strip()
                }
        ret.append(con)

    return json.dumps(ret)

def anifo2(URL):
    URL = d_url(URL)
    #URL = 'https://www.oploverz.in/series/one-piece-sub-indo/'
    # scraper = cfscrape.create_scraper()
    scraper = cloudscraper.create_scraper()
    soup = BeautifulSoup(scraper.get(URL).content, 'html.parser')
    return soup.prettify(formatter="html5")

def get_vid2(URL):
    URL = d_url(URL)
    # scraper = cfscrape.create_scraper()
    scraper = cloudscraper.create_scraper()
    soup = BeautifulSoup(scraper.get(URL).content, 'html.parser')
    return soup.prettify(formatter="html5")

def menimea():
    URL = "http://menime.herokuapp.com/"
    # scraper = cfscrape.create_scraper()
    scraper = cloudscraper.create_scraper()
    soup = BeautifulSoup(scraper.get(URL).content, 'html.parser')
    return soup.prettify(formatter="html5")

# URL = "https://oploverz.bz/anime/one-piece/" 
# URL = "https://oploverz.bz/anime/captain-tsubasa-2018/" 
# URL = "https://www.animeindo.cc/dragon-ball-episode-001-subtitle-indonesia/" 

#_url(URL)
#URL = 'https://www.oploverz.in/series/one-piece-sub-indo/'
# scraper = cfscrape.create_scraper()
# scraper = cloudscraper.create_scraper()
# soup = BeautifulSoup(scraper.get(URL).content, 'html.parser')

"""
foreach ($html->find(".playeriframe") as $iframe) {
        return $iframe->src;
    }

"""
al = ["https://www84.zippyshare.com/v/tLbmh3b4/file.html", "https://www111.zippyshare.com/v/tWgdDLU2/file.html", "https://www32.zippyshare.com/v/EJ5tE51o/file.html", "https://www32.zippyshare.com/v/fB7sIk07/file.html", "https://www32.zippyshare.com/v/MsfPEuqf/file.html", "https://www32.zippyshare.com/v/tDeS2mRO/file.html", "https://www32.zippyshare.com/v/BVBUekHS/file.html", "https://www32.zippyshare.com/v/phMOgbCi/file.html", "https://www32.zippyshare.com/v/4KpnM7tt/file.html", "https://www60.zippyshare.com/v/oYwjuclJ/file.html", "https://www60.zippyshare.com/v/gjxwlsUN/file.html", "https://www60.zippyshare.com/v/TFoX8yHW/file.html", "https://www60.zippyshare.com/v/diKWG5p0/file.html", "https://www60.zippyshare.com/v/pKOo52IT/file.html", "https://www60.zippyshare.com/v/v4Pmthu6/file.html", "https://www60.zippyshare.com/v/aYj0LDGt/file.html", "https://www60.zippyshare.com/v/EwoZQiUp/file.html", "https://www60.zippyshare.com/v/DQB6e3WO/file.html", "https://www60.zippyshare.com/v/B18ghaO5/file.html"];
scraper = cloudscraper.create_scraper()
for lk in al:
    print(lk)
    soup = BeautifulSoup(scraper.get(lk).content, 'html.parser')
    link = soup.find("a",  {"id": "dlbutton"})
    print(link)
    print(link.get('href'))
    break



# listinfo = soup.find('div', class_='listinfo')
# img_des = soup.find('div', class_='imgdesc')
# img = img_des.findChildren("img" , recursive=False)