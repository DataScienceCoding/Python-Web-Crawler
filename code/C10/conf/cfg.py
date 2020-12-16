import configparser
import os


class Conf():
    """
    创建配置类
    """
    def __init__(self):
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'conf.ini'))
        cfg = configparser.ConfigParser()
        cfg.read(path)
        self._conf = cfg

    def section(self, opt):
        return self._conf._sections[opt]
