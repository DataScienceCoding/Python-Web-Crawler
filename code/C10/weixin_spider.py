from pkg.redis import RedisCli
from conf.cfg import Conf
from pkg.ip_proxy import ProxyPool
from pkg.util import browserwraper, httpget
from urllib.parse import urlencode


def getweixinpage(pool: ProxyPool, keyword, pagenumber=1):
    param = {
        'type': '2',
        's_from': 'input',
        'query': keyword,
        'ie': 'utf8',
        '_sug_': 'n',
        '_sug_type_': ''
    }

    if pagenumber > 1:
        param['page'] = pagenumber
    headers = {
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Encoding': 'gzip',
        'Content-Type': 'text/html; charset=utf-8',
        'Date': 'Thu, 10 Dec 2020 07:25:23 GMT',
        'Expires': 'Thu, 10 Dec 2020 07:25:23 GMT',
        'Server': 'nginx',
        'Set-Cookie': 'black_passportid=1; domain=.sogou.com; path=/; expires=Thu, 01-Dec-1994 16:00:00 GMT',
        'Transfer-Encoding': 'chunked',
        'Vary': 'Accept-Encoding',
        'X-Frame-Options': 'allow-from sogou-inc.com',
        'x_ad_pagesize': 'adpagesize=0',
        'x_log_ext': 'ret=1&ret_exp=1&user_level=51&token=2EE5BC96D5E11D7C0C08BA1BBAFAA8600D07C5D05FD1CD63',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'ABTEST=0|1607583558|v1; SNUID=D5E11D7C0C08BA1BBAFAA8600D07C5D0; IPLOC=CN3300; SUID=D8EC11704018960A000000005FD1C746; JSESSIONID=aaaeanwvai68Zdhze4Eyx; SUV=0025C2A97011ECD85FD1C7483080E622; SUID=D8EC11702C18960A000000005FD1C752; weixinIndexVisited=1; ppinf=5|1607583630|1608793230|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyNzolRTYlQUMlQTIlRTQlQjklOTAlRTklQTklQUN8Y3J0OjEwOjE2MDc1ODM2MzB8cmVmbmljazoyNzolRTYlQUMlQTIlRTQlQjklOTAlRTklQTklQUN8dXNlcmlkOjQ0Om85dDJsdU9Zam1oaVltbnJtSGhpQnJPX3lSVElAd2VpeGluLnNvaHUuY29tfA; pprdig=xMbSMSzr5yZb0AXNxbfz-l3xT14nVK-k2ddiKs5RDQPum1-3p-TCROJVQ-fneVqdb47Ba_BHbvGc-ap3s146mY_ega9-LdTHLA5l__3u3EOEoZwSrdAzE-v0Xa5WanRsXlnG7bJ918aXhOPUyXYqQtRlbzBxZJhgaCnMXfX9WCs; ppinfo=544795b0fa; passport=5|1607583630|1608793230|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToyNzolRTYlQUMlQTIlRTQlQjklOTAlRTklQTklQUN8Y3J0OjEwOjE2MDc1ODM2MzB8cmVmbmljazoyNzolRTYlQUMlQTIlRTQlQjklOTAlRTklQTklQUN8dXNlcmlkOjQ0Om85dDJsdU9Zam1oaVltbnJtSGhpQnJPX3lSVElAd2VpeGluLnNvaHUuY29tfA|bdfc681a3f|xMbSMSzr5yZb0AXNxbfz-l3xT14nVK-k2ddiKs5RDQPum1-3p-TCROJVQ-fneVqdb47Ba_BHbvGc-ap3s146mY_ega9-LdTHLA5l__3u3EOEoZwSrdAzE-v0Xa5WanRsXlnG7bJ918aXhOPUyXYqQtRlbzBxZJhgaCnMXfX9WCs; sgid=04-48806141-AVicRx46z6Nhd2YDMGhT9Gyk; ppmdig=160758363000000086b201db024213f1e06eb43135f85030',
        'Host': 'weixin.sogou.com',
        'Referer': 'https://weixin.sogou.com/weixin?type=2&query=NBA&ie=utf8&s_from=input&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=0&sourceid=sugg&sut=0&sst0=1607583657856&lkt=0%2C0%2C0&p=40040108',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }

    proxyip = pool.random()
    global proxies
    url = 'http://weixin.sogou.com/weixin?'+urlencode(param)
    if proxyip:
        proxies = {
            'http': 'http://' + proxyip,
            'https': 'https://' + proxyip
        }

        resp = httpget(url, headers=headers, proxies=proxies)
        if resp:
            pool.updatescore(proxyip, resp['elapsed'])
            return resp['body']
    else:
        resp = httpget(url, headers=headers)
        if resp:
            return resp['body']


conf = Conf()
redis = RedisCli(conf)
pool = ProxyPool(redis)
# print(getweixinpage(pool, '马拉多纳'))

param = urlencode({
    'type': '2',
    'query': '马拉多纳'
})
url = 'http://weixin.sogou.com/weixin?{}'.format(param)
proxyip = pool.random()
browser = browserwraper('--proxy-server=http://{}'.format(proxyip))
print(browser.get(url))
