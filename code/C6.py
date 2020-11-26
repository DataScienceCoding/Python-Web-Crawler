# import requests
# from requests import RequestException
from urllib import request, parse
from urllib.error import URLError
import json
from lxml import etree
# from requests import cookies


# def savehtml(name, url, header, data=None, jar=None):
#     try:
#         response = requests.get(url, header, data=data, cookies=jar)
#         if response.status_code == 200:
#             with open(name, mode='w', encoding='utf-8') as f:
#                 f.write(response.text)
#         else:
#             print(response.reason)
#     except RequestException as e:
#         print(e.reason)

def gethtmltofile(name, url, header={}, data=None):
    try:
        if data:
            data = bytes(parse.urlencode(data), encoding='utf8')
        req = request.Request(url=url, data=data, headers=header, method='GET')
        response = request.urlopen(req)
        if response.status == 200:
            with open(name, mode='w', encoding='utf-8') as f:
                f.write(str(response.read().decode('utf-8')))
        else:
            print(response.reason)
    except URLError as e:
        print(e.reason)


def parsehtml(pattern, name):
    html = etree.parse(name, etree.HTMLParser())
    return html.xpath(pattern)


def parsejson(fname):
    with open(fname, 'r', encoding="utf-8") as file:
        str = file.read()
        data = json.loads(str)
        print(data['data'][0])



if __name__ == "__main__":
    # header = {

    # }
    # header = {
    #     'cache-control': 'no-cache, no-store, must-revalidate, private, max-age=0',
    #     'content-encoding': 'gzip',
    #     'content-type': 'application/json',
    #     'date': 'Thu, 29 Oct 2020 07:07:02 GMT',
    #     'expires': 'Thu, 01 Jan 1970 08:00:00 CST',
    #     'pragma': 'no-cache',
    #     'referrer-policy': 'no-referrer-when-downgrade',
    #     'server': 'CLOUD ELB 1.0.0',
    #     'set-cookie': 'KLBRSID=031b5396d5ab406499e2ac6fe1bb1a43|1603955222|1603952885; Path=/',
    #     'status': '200',
    #     'vary': 'Accept-Encoding',
    #     'x-ab-trigger': 'se_timescore=0',
    #     'x-backend-response': '0.346',
    #     'x-cache-lookup': 'Cache Miss',
    #     'x-cdn-provider': 'tencent',
    #     'x-idc-id': '2',
    #     'x-lb-timing': '0.352',
    #     'x-nws-log-uuid': '3794396044848039424',
    #     'x-secng-response': '0.35000014305115',
    #     'x-udid': 'ABBX4FrWHBKPTtc9x-ZTtcYl1Uyzfj4KEY8=,'
    # }
    # jar = requests.cookies.RequestsCookieJar()
    # cookies =
    # for cookie in cookies.split(';'):
    #     key, value = cookie.split('=', 1)
    #     jar.set(key, value)
    # data = {
    #     't': 'general',
    #     'q': '爬虫',
    #     'correction': 1,
    #     'offset': 0,
    #     'limit': 20,
    #     'lc_idx': 0,
    #     'show_all_topics': 0
    # }
    fname = 'code/toutiao.html'
    # gethtmltofile('code/toutiao.html', 'https://www.toutiao.com/api/search/content/?aid=24&app_name=web_search&offset=0&format=json&keyword=%E9%A3%8E%E6%99%AF&autoload=true&count=20&en_qc=1&cur_tab=1&from=search_tab&pd=synthesis&timestamp=1603958482286&_signature=_02B4Z6wo00f01hsI1xwAAIBCDYP2W-L5esobDdOAANllCyNDnVhoeJ491c7rLv1ScGqt2beHsUxguFul4uIwYHRajHZSGVfQkwlMAdfsXDpXARveCCbT1mnynG4rOq5G56UQzHxyID4xeXyK02')

    parsejson(fname)