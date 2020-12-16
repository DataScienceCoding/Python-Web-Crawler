import requests
from requests import RequestException
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def httpget(url, encoding='utf-8', headers=None, proxies=None):
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        if response.status_code == 200:
            response.encoding = encoding
            return {
                'body': response.text,
                'elapsed': response.elapsed.total_seconds()
            }
        print('响应失败状态: ', response.status_code)
        return None
    except RequestException as e:
        print('请求失败', e)
        return None


def browserwraper(*args):
    opts = Options()
    # opts.add_argument('--headless')
    opts.add_argument('--disable-gpu')
    for arg in args:
        opts.add_argument(arg)
    return webdriver.Chrome(executable_path=r'D:\ENV\chromedriver.exe', options=opts)
