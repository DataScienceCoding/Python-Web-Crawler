import configparser
import os


# root = os.path.dirname(os.path.abspath('.'))
# path = os.path.join(root, "code/conf.ini")
print(os.getcwd())
cfg = configparser.ConfigParser()
cfg.read('code/C9/conf.ini')

print(cfg.sections())
print(cfg.get('proxy-pool', 'url'))


print(cfg.get('mysql', 'host'))
