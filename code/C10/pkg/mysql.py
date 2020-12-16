import pymysql
from conf.cfg import Conf


class MysqlCli():
    def __init__(self):
        conf = Conf()
        option = conf.section('mysql')
        try:
            self._db = pymysql.connect(host=option['host'],
                                       port=int(option['port']),
                                       user=option['username'],
                                       password=option['password'])
            self.cursor = self._db.cursor()
        except Exception as e:
            print(e.reason())

    # def execute(self, sql, *arg):
    #     return self._db.execute(sql, arg)

    def __del__(self):
        print('Mysql will be closed.')
        self._db.close()
