
from pkg.exception import QueueFullExceptin
from pkg.redis import RedisCli
from random import choice

PROXY_KEY = 'IP_PROXY'
VALID_MAX_SCORE = 20
VALID_MIN_SCORE = 0
POOL_CAP = 1000


class ProxyPool():
    def __init__(self, cli: RedisCli):
        self._cli = cli

    def add(self, ip, score):
        if self._cli.db().zcard(PROXY_KEY) == POOL_CAP:
            raise QueueFullExceptin()
        if not self._cli.exists(ip):
            self._cli.db().zadd(PROXY_KEY, {ip: score})

    def updatescore(self, ip, score):
        self._cli.db().zadd(PROXY_KEY, {ip: score})

    def random(self):
        result = self._cli.db().zrangebyscore(PROXY_KEY, VALID_MIN_SCORE, VALID_MAX_SCORE)
        if len(result):
            return choice(result)
        else:
            return None

    def decrease(self, proxy):
        """
        代理值减一分（即响应系数减1），大于最大响应值则删除
        :param proxy: 代理
        """
        score = self._cli.db().zscore(PROXY_KEY, proxy)
        if score and score < VALID_MAX_SCORE:
            print('代理', proxy, '当前响应系数', score, '减1')
            return self.db()._cli.zincrby(PROXY_KEY, proxy, -1)
        else:
            print('代理', proxy, '当前响应系数', score, '移除')
            return self.db()._cli.zrem(PROXY_KEY, proxy)

    def exists(self, proxy):
        """
        判断是否存在
        :param proxy: 代理
        :return: 是否存在
        """
        return self._cli.db().zrank(PROXY_KEY, proxy) is not None

    def all(self):
        return self._cli.db().zrangebyscore(PROXY_KEY, VALID_MIN_SCORE, VALID_MAX_SCORE)
