from pkg.util import httpget
from conf.cfg import Conf
import json
import time
from pkg.exception import InvalidIPExceptin, QueueFullExceptin
from pkg.ip_proxy import ProxyPool
from telnetlib import Telnet

# from pkg.mysql import MysqlCli
from pkg.redis import RedisCli

# print(redis.get(key))

# db = MysqlCli()
# db.cursor.execute('USE spiders')
# db.cursor.execute('select count(*) from station')
# row = db.cursor.fetchone()
# print(row)


def testproxyip(addr: str):
    ip, port = addr.split(":", 1)
    try:
        with Telnet(ip, port, timeout=20):
            pass
    except Exception:
        raise InvalidIPExceptin()


def fillproxyqueue(conf: Conf, pool: ProxyPool):
    global proxy
    while True:
        try:
            proxy = getproxy(conf)
            if proxy:
                testproxyip(proxy)
                pool.add(proxy, 0)  # 无异常则放到队列中
        except QueueFullExceptin:
            print('队列已满 ')
            time.sleep(2 * 60 * 60)  # 队列满了就休息两小时
        except InvalidIPExceptin:
            print('无效IP: ', proxy)
        finally:
            time.sleep(5)


def getproxy(conf: Conf):
    url = conf.section('proxy-url')['url']
    rep = httpget(url)
    if rep:
        return json.loads(rep['body'])['proxy']
    return None


conf = Conf()
redis = RedisCli(conf)
pool = ProxyPool(redis)
fillproxyqueue(conf, pool)
