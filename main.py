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
URL = "https://oploverz.bz/anime/captain-tsubasa-2018/" 

#_url(URL)
#URL = 'https://www.oploverz.in/series/one-piece-sub-indo/'
# scraper = cfscrape.create_scraper()
scraper = cloudscraper.create_scraper()
soup = BeautifulSoup(scraper.get(URL).content, 'html.parser')


desc = soup.find("div", class_="entry-content")
listinfo = soup.find('div', class_='ninfo')
img = soup.find('img', class_='wp-post-image')
# print(desc)
# print("<br>")
# print(listinfo)
# print("<br>")
# print(img['src'])

b = listinfo.prettify(formatter="html5") if listinfo else ""
d = b.replace('"', "\"")
f = html.escape(d)

print(f)



# listinfo = soup.find('div', class_='listinfo')
# img_des = soup.find('div', class_='imgdesc')
# img = img_des.findChildren("img" , recursive=False)