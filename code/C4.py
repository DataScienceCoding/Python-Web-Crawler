from pyquery import PyQuery as pq

text = '''
<div id="container">
  <ul class="list">
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''
doc = pq(text)
li = doc('#container .list li')
print(li, type(li), "\n")

print("find方法查找所有子孙节点\n", li.find('a'))
print("children方法查找所有儿子节点\n", doc(".list").children(".active"))
print("parent方法查找父亲节点\n", li.parent())
print("parents方法查找祖先节点\n", li.parents())
print("siblings方法查找兄弟节点\n", li.siblings())
print("items方法用于遍历节点\n", [item for item in li.items()])
print("attr方法用于获取属性\n", doc('.item-0.active a').attr('href'))
print("text方法用于获取文本\n", doc('.item-0.active a').text())
print("html方法用于获取含HTML文本\n", doc('.item-0.active a').html())


print("\nremoveClass、addClass方法可操作class属性")
ai = doc(".item-0.active")
ai.removeClass('active')
print(ai)
ai.addClass('active')
print(ai)
ai.find('span').remove()
print(ai.text())

# from lxml import etree

# text = '''
# <div>
#   <ul>
#     <li class="item-0">
#       <a href="link1.html" class="first-link">
#         <span>first item</span>
#       </a>
#     </li>
#     <li class="item-1">
#       <a href="link2.html">
#         <span>second item</span>
#       </a>
#     </li>
#     <li class="item-inactive grey-item">
#       <a href="link3.html">
#         <span>third item</span>
#       </a>
#     </li>
#     <li class="item-1">
#       <a href="link4.html">
#         <span>fourth item</span>
#       </a>
#     </li>
#     <li class="item-0"><a href="link5.html"><span>fifth item</a>
#   </ul>
# </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))

# print("\n选取父节点及属性匹配——获取链接link3.html对应a标签的父亲节点的class属性")
# result = html.xpath('//a[@href="link3.html"]/../@class')
# print(result)

# print("\n获取文本")
# result = html.xpath('//li[@class="item-0"]//text()')
# print(result)

# print("\n获取所有子孙节点的文本")
# result = html.xpath('//li[@class="item-0"]//text()')
# print(result)

# print("\n获取属性")
# result = html.xpath('//li/a/@href')
# print(result)

# print("\n多值属性的匹配")
# result = html.xpath('//li[@class="grey-item"]//span/text()')
# result = html.xpath('//li[contains(@class, "grey-item")]//span/text()')
# print(result)

# print("\n多个属性的匹配")
# result = html.xpath('//li/a[@href="link1.html" and @class="first-link"]/span/text()')
# print(result)

# print('\n按序匹配')
# result = html.xpath('//li[1]//span/text()')
# print(result)
# result = html.xpath('//li[last()]//span/text()')
# print(result)
# result = html.xpath('//li[position()<3]//span/text()')
# print(result)
# result = html.xpath('//li[last()-2]//span/text()')
# print(result)

# print("\n按节点关系匹配")
# result = html.xpath('//li[1]/ancestor::*')
# print(result)
# result = html.xpath('//li[1]/ancestor::div')
# print(result)
# result = html.xpath('//li[1]/attribute::*')
# print(result)
# result = html.xpath('//li[1]/child::a[@href="link1.html"]')
# print(result)
# result = html.xpath('//li[1]/descendant::span')
# print(result)
# result = html.xpath('//li[1]/following::*[2]')
# print(result)
# result = html.xpath('//li[1]/following-sibling::*')
# print(result)

# from lxml import etree

# html = etree.parse('code/demo.html', etree.HTMLParser())
# result = etree.tostring(html)
# print(result.decode('utf-8'))


# import re


# text = """张良: 13575457890 澎湖湾2号

# 李白: 15978239086 蜀道115号
# 杜甫: 18623456723 黄鹤楼镇11号


# 范仲淹: 18978236745 贝尔加湖畔100号"""

# entries = re.split("\n+", text)
# print(entries)
# phone_book = [re.split(":? ", entry, 3) for entry in entries]
# print(phone_book)

# text = '''010-58991938
# 客服邮箱：service@weather.com.cn广告服务：010-58991910京ICP证010385号
# 客服热线：400-6000-121商务合作：010-58991806
# 增值电信业务经营许可证B2-20050053
# '''

# pattern = r'(0\d{3})-([^0]\d{6})|(0\d{2})-([^0]\d{7})'
# result = re.match(pattern, text)
# print(result, '> match\n')
# if result:
#     print(result.group(), '> match\n')
# result = re.search(pattern, text)
# print(result, '> search\n')
# if result:
#     print(result.group(), '> search\n')
# result = re.findall(pattern, text)
# print(result, '> findall\n')


# import requests