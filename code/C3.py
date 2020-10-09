import json
import requests
from requests.exceptions import RequestException
import re
import time
import random


def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }


def write_html(offset, html):
    with open("code/{}.html".format(offset), mode='w+', encoding='utf-8') as f:
        f.write(html)


def write_result(content):
    with open('result.txt', 'a') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    write_html(offset, html)
    for item in parse_one_page(html):
        print(item)
        write_result(item)


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)
        time.sleep(random.randint(1, 4))

# import re

# content = 'Hello, my phone number is 13512345678 and email is carmeltop@qq.com, \
#     and my website is https://github.com/carmel.'

# result = re.search('(1[3456789]\d{9})', content, re.S)
# if result:
#     print(result.group())
#     print(result.group(1))
#     print(result.span(), '\n')

# result = re.search('([a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+))+', content, re.S)
# if result:
#     print(result.group(1))

# html = '''<div id="songs-list">
#     <h2 class="title">经典老歌</h2>
#     <p class="introduction">
#         经典老歌列表
#     </p>
#     <ul id="list" class="list-group">
#         <li data-view="2">一路上有你</li>
#         <li data-view="7">
#             <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
#         </li>
#         <li data-view="4" class="active">
#             <a href="/3.mp3" singer="齐秦">往事随风</a>
#         </li>
#         <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
#         <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
#         <li data-view="5">
#             <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
#         </li>
#     </ul>
# </div>'''

# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(results)
# for result in results:
#     print(result)
#     print(result[0], result[1], result[2], '\n')

# html = re.sub('<a.*?>|</a>', '', html)
# print(html)
# results = re.findall('<li.*?>(.*?)</li>', html, re.S)
# for result in results:
#     print(result.strip(), '\n')

# content1 = '2016-12-15 12:00'
# content2 = '2016-12-17 12:55'
# content3 = '2016-12-22 13:21'
# pattern = re.compile('\d{2}:\d{2}')
# result1 = re.sub(pattern, '', content1)
# result2 = re.sub(pattern, '', content2)
# result3 = re.sub(pattern, '', content3)
# print(result1, result2, result3, '\n')

# content = 'Hello 1234567 World_This is a Regex Demo'
# result = re.match('^Hello\s(\d+)\sWorld', content, re.I)
# print(result)
# print(result.group())
# print(result.group(1))
# print(result.span())
# print(len('Hello 1234567 World'))

# 抓取网页
# headers = {
#     'User-Agent':
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# r.encoding = r.apparent_encoding
# pattern = re.compile(
#     'ExploreRoundtableCard-title|ExploreSpecialCard-title.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles, '\n')

# 抓取文件
# r = requests.get("https://github.com/favicon.ico")
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

# r = requests.get('https://www.jianshu.com')
# print(r.status_code)
# print(r.headers)
# print(r.cookies)
# print(r.url)
# print(r.history)

# 文件上传
# files = {'file': open('favicon.ico', 'rb')}
# r = requests.post("http://httpbin.org/post", files=files)
# print(r.text, '\n')

# # 获取cookie
# r = requests.get("https://www.baidu.com")
# for key, value in r.cookies.items():
#     print("{0}={1}\n".format(key, value))

# header添加cookie
# cookies = 'q_c1=31653b264a074fc9a57816d1ea93ed8b|1474273938000|1474273938000; d_c0="AGDAs254kAqPTr6NW1U3XTLFzKhMPQ6H_nc=|1474273938"; __utmv=51854390.100-1|2=registration_date=20130902=1^3=entry_date=20130902=1;a_t="2.0AACAfbwdAAAXAAAAso0QWAAAgH28HQAAAGDAs254kAoXAAAAYQJVTQ4FCVgA360us8BAklzLYNEHUd6kmHtRQX5a6hiZxKCynnycerLQ3gIkoJLOCQ==";z_c0=Mi4wQUFDQWZid2RBQUFBWU1DemJuaVFDaGNBQUFCaEFsVk5EZ1VKV0FEZnJTNnp3RUNTWE10ZzBRZFIzcVNZZTFGQmZn|1474887858|64b4d4234a21de774c42c837fe0b672fdb5763b0'
# jar = requests.cookies.RequestsCookieJar()
# headers = {
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
# }

# for cookie in cookies.split(';'):
#     key, value = cookie.split('=', 1)
#     jar.set(key, value)
# r = requests.get("http://www.zhihu.com", cookies=jar, headers=headers)
# print(r.text)

# 指定ca证书
# response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
# print(response.status_code)

# 指定代理
# proxies = {"http": "127.0.0.1:8888"}

# r = requests.get("https://www.taobao.com", proxies=proxies)
# print(r.status_code)

# from urllib.robotparser import RobotFileParser
# from urllib.request import urlopen

# rp = RobotFileParser()
# rp.set_url('http://www.jianshu.com/robots.txt')
# rp.read()
# print(rp.can_fetch('*', 'https://www.jianshu.com/p/b67554025d7d'))
# print(rp.can_fetch('*', "http://www.jianshu.com/search?q=python&page=1&type=collections"))

# rp.parse(urlopen('https://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
# print(rp.can_fetch('*', 'https://www.jianshu.com/p/b67554025d7d'))
# print(rp.can_fetch('*', "https://www.jianshu.com/search?q=python&page=1&type=collections"))

# from urllib.parse import urlparse, urlunparse, urlsplit, urlunsplit, \
#     urljoin, urlencode, parse_qs, parse_qsl, quote, unquote

# url = 'https://www.baidu.com/index.html;user?id=5#comment'
# print(urlparse(url, allow_fragments=False), '\n')
# # 目标地址解析成scheme, netloc, path, params, query, fragments六个部分
# print(urlsplit(url, allow_fragments=False), '\n')
# # 目标地址解析成scheme, netloc, path, query, fragments五个部分

# data = ['http', 'wwww.baidu.com', 'index.html', 'user', 'a=6', 'comment']
# print(urlunparse(data), '\n')

# data = ['http', 'wwww.baidu.com', 'index.html', 'a=6', 'comment']
# print(urlunsplit(data), '\n')

# print(urljoin(base='http://www.baidu.com', url='FAQ.html'))
# print(urljoin('http://www.baidu.com', 'https://www.zhihu.com/FAQ.html'))
# print(urljoin('http://www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com', '?category=2#comment'))
# print(urljoin('www.baidu.com#comment', '?category=2'), '\n')

# params = {
#     'name': 'Vector',
#     'age': 30
# }
# url = urlencode(params)
# print(url, '\n')
# print(parse_qs(url), '\n')
# print(parse_qsl(url), '\n')

# quote_word = quote('中国')
# print('https://www.baidu.com/s?wd={0}'.format(quote_word), '> quote_word\n')
# print(unquote(quote_word), '> unquote\n')

# from urllib import request as rq, parse as pr
# from urllib.error import URLError
# from urllib.request import ProxyHandler, build_opener

# request = rq.Request('https://python.org')
# response = rq.urlopen(request)
# print(response.read().decode('utf-8'))

# url = 'http://httpbin.org/post'
# headers = {
#     'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
#     'Host': 'httpbin.org'
# }

# data = bytes(pr.urlencode({'name': 'Germey'}), encoding='utf-8')
# request = rq.Request(url, data, headers=headers, method='POST')
# request.add_header('Cookie', 'Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1602235479')
# response = rq.urlopen(request)
# print(response.read().decode('utf-8'))

# proxy_handler = ProxyHandler({'http': '127.0.0.1:8888'})
# opener = build_opener(proxy_handler)

# try:
#     response = opener.open(rq.Request("http://www.baidu.com/"))
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

# import socket
# import urllib.parse as up
# import urllib.request as ur
# import urllib.error as ue

# data = bytes(up.urlencode({'word': 'hello'}), encoding='utf-8')
# try:
#     response = ur.urlopen('http://httpbin.org/post', data=data, timeout=3)
#     print(response.read().decode('utf-8'))
# except ue.URLError as e:
#     if (isinstance(e.reason, socket.timeout)):
#         print('Time is out')

# import urllib.request as ur

# response = ur.urlopen('https://www.python.org')
# html = response.read().decode('utf-8')
# # print(html)

# with open('code/python.org.html', mode='w+') as f:
#     f.write(html)
# print(f.closed)

# print(help(type(response)))
# print(response.status, '> response.status\n')
# print(response.getheaders(), '> response.getheaders()\n')
# print(response.getheader('Server'), "> response.getheader('Server')\n")
