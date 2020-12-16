
import redis
import sys
from conf.cfg import Conf


class RedisCli():
    def __init__(self, conf: Conf):
        """
        RedisCli初始化操作
        """
        option = conf.section('redis')
        try:
            pool = redis.ConnectionPool(host=option['host'], port=option['port'], password=option['password'], decode_responses=True)
            self._redis = redis.Redis(connection_pool=pool)
        except Exception as e:
            print(e.reasion)
            sys.exit(1)

    def db(self):
        return self._redis

    def set(self, key, val, timeout=0):
        self._redis.set(key, val)
        if timeout != 0:
            self._redis.expire(key, timeout)

    def get(self, key):
        return self._redis.get(key)

    def exists(self, key):
        return self._redis.exists(key)
