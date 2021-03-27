import requests
from bs4 import BeautifulSoup
import re


def paqu(search_keyword: str):  # 传入想要搜索的东西
    search_url = 'https://www.okzyw.net/index.php?m=vod-search'  # 发送请求的链接，注意不是网址
    serach_params = {
        'm': 'vod-search'
    }
    serach_headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        'Referer': 'http://www.jisudhw.com/',
        'Origin': 'http://www.jisudhw.com',
        'Host': 'www.jisudhw.com'
    }
    serach_datas = {
        'wd': search_keyword,
        'submit': 'search'
    }

    r = requests.post(url=search_url, params=serach_params, headers=serach_headers, data=serach_datas)

    r.encoding = 'utf-8'
    search_html = BeautifulSoup(r.text, 'lxml')
    search_spans = search_html.find_all('span', class_='xing_vb4')
    zidian = {}
    lll = []
    mmm = []
    for span in search_spans:
        url = span.a.get('href')
        url = str(url)
        url = url.replace('?', '')
        name = span.a.string
        mmm.append(name)
        lll.append(url)
        dict2 = {name: url}
        zidian.update(dict2)

    return zidian  # 返回名字和链接


def xiangqing(url):
    url = 'http://www.okzyw.net/?' + url
    rrr = requests.get(url)
    rrr.encoding = 'utf-8'
    rrr = str(rrr.text)
    matches = re.finditer(r"/>.{0,10}http.*<", rrr)

    cc = []
    bb = {}
    pp = []
    ll = []
    for matchNum, match in enumerate(matches, start=1):
        cc.append(match.group().replace('/>', '').replace('<', ''))

    for a in cc:
        a = a.split('$', 1)
        x = a[0]
        y = a[1]
        pp.append(a[0])
        ll.append(a[1])
        bb.update({x: y})
    return pp, ll
