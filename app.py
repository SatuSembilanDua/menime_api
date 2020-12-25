import flask
from flask import request, jsonify, json
from bs4 import BeautifulSoup
import cfscrape
import html
import base64

app = flask.Flask(__name__)
app.config["DEBUG"] = True

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
    scraper = cfscrape.create_scraper()
    soup = BeautifulSoup(scraper.get(URL).content, 'html.parser')

    desc = soup.find('span', class_='desc')
    listinfo = soup.find('div', class_='listinfo')
    img_des = soup.find('div', class_='imgdesc')
    img = img_des.findChildren("img" , recursive=False)

    a = desc.prettify(formatter="html5")
    b = listinfo.prettify(formatter="html5")
    c = a.replace('"', "'")
    d = b.replace('"', "'")
    e = html.escape(c)
    f = html.escape(d)
    ret = {'desc':e,'info':f,'img':img[0]["src"]}
    jsona = json.dumps(ret)
    return jsona

def get_vid(URL):
    URL = d_url(URL)
    scraper = cfscrape.create_scraper()
    soup = BeautifulSoup(scraper.get(URL).content, 'html.parser')
    
    iframe = soup.find('iframe', class_='idframe')
    #a = iframe.prettify(formatter="html5")
    # e = html.escape(a)
    return iframe['src']

@app.route('/', methods=['GET'])
def home():
    return "<h1>Menime</h1><p>This site is a prototype API for menime. !</p>"

@app.route('/anime_info/<link_url>', methods=['GET'])
def anime_info(link_url):
    return anifo(link_url)

@app.route('/list_anime/<link_url>', methods=['GET'])
def list_anime(link_url):
    return get_vid(link_url)

@app.route('/anin/', methods=['GET'])
def anin():
    lr = "aHR0cHM6Ly93d3cub3Bsb3ZlcnouaW4vc2VyaWVzL29uZS1waWVjZS1zdWItaW5kby8"
    return anifo(lr)

@app.route('/la/', methods=['GET'])
def la():
    lr = "aHR0cHM6Ly93d3cub3Bsb3ZlcnouaW4vb25lLXBpZWNlLWVwaXNvZGUtOTU0LXN1YnRpdGxlLWluZG9uZXNpYS8"
    return list_anime(lr)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

#


"""
print(anifo())

https://www.oploverz.in/one-piece-episode-954-subtitle-indonesia
aHR0cHM6Ly93d3cub3Bsb3ZlcnouaW4vb25lLXBpZWNlLWVwaXNvZGUtOTU0LXN1YnRpdGxlLWluZG9uZXNpYS8

print(listinfo.prettify())



"""