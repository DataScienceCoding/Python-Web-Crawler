import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options


def browserwraper(*args):
    opts = Options()
    # opts.add_argument('--headless')
    opts.add_argument('--disable-gpu')
    for arg in args:
        opts.add_argument(arg)
    return webdriver.Chrome(executable_path=r'D:\ENV\chromedriver.exe', options=opts)


browser = browserwraper()

try:
    browser.get('https://www.zhihu.com/explore')
    wait = WebDriverWait(browser, 35)
    classname = 'ExploreHomePage-roundtables'
    wait.until(ec.presence_of_element_located((By.CLASS_NAME, classname)))
    search = browser.find_element_by_css_selector('input[aria-activedescendant="AutoComplete2--1"]')
    print(search.get_attribute('placeholder'))
    content = browser.find_element_by_class_name(classname)
    roundtable = browser.find_elements_by_class_name('ExploreHomePage-roundtableCard')
    for i in roundtable:
        # print(i.text, '\n')
        print('主题: {}, 嘉宾人数: {}, 关注人数: {}'.format(
            i.find_element_by_class_name('ExploreRoundtableCard-title').text,
            i.find_element_by_css_selector('.ExploreRoundtableCard-guests span').text,
            i.find_element_by_css_selector('.ExploreRoundtableCard-count span').text
        ))

        # print('金额: ', i.find_element_by_xpath('//div[@class="q-type"]/div[contains(@class,"q-price")]/strong').text)
        # print('规则: ', i.find_element_by_xpath('//div[@class="q-type"]/div[contains(@class,"q-price")]/span').text)
    # print(coupon.text)
finally:
    browser.close()

# try:
#     browser.get('https://www.jd.com/')
#     wait = WebDriverWait(browser, 35)
#     path = '//a[@aria-lable="优惠券"]'
#     wait.until(ec.presence_of_element_located((By.XPATH, path)))
#     coupon = browser.find_element_by_xpath(path)
#     # 进入优惠券页面
#     coupon.click()
#     time.sleep(3)
#     browser.switch_to.window(browser.window_handles[1])

#     # 滚动到底部
#     # js = '''
#     # window.scrollTo(0, document.body.scrollHeight)
#     # '''
#     # browser.execute_script(js)
#     SCROLL_PAUSE_TIME = 0.5

#     # Get scroll height
#     last_height = browser.execute_script("return document.body.scrollHeight")
#     while True:
#         # Scroll down to bottom
#         browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#         # Wait to load page
#         time.sleep(SCROLL_PAUSE_TIME)

#         # Calculate new scroll height and compare with last scroll height
#         new_height = browser.execute_script("return document.body.scrollHeight")
#         if new_height == last_height:
#             break
#         last_height = new_height
#     # wait.until(ec.presence_of_all_elements_located((By.CLASS_NAME, 'quan-item')))
#     quans = browser.find_elements_by_class_name('quan-item')
#     for i in quans:
#         print(i.text, '\n')
#         # print('金额: ', i.find_element_by_xpath('//div[@class="q-type"]/div[contains(@class,"q-price")]/strong').text)
#         # print('规则: ', i.find_element_by_xpath('//div[@class="q-type"]/div[contains(@class,"q-price")]/span').text)
#     # print(coupon.text)
# finally:
#     browser.close()

# browser = headlessbrowser()
# try:
#     # 访问页面
#     browser.get('https://www.baidu.com')
#     # 查找页面中id为'kw'的输入框
#     input = browser.find_element_by_id('kw')
#     # 在输入框中输入Python关键字
#     input.send_keys('Python')
#     # 触发回车键
#     input.send_keys(Keys.ENTER)
#     # 等待浏览器执行10秒
#     wait = WebDriverWait(browser, 10)
#     # 不断检查页面id为content_left的DOM元素是否存在直到其渲染完成
#     wait.until(ec.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()
