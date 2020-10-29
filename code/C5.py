from pymongo import MongoClient, ASCENDING
# from bson.objectid import ObjectId

client = MongoClient(host='localhost',
                     port=27017,
                     username='Admin',
                     password='admin')
# 读取所有数据库
dblist = client.list_database_names()
DBName = 'spiders'
print('{}数据库存在'.format(DBName)) if DBName in dblist else print(
    '{}数据库不存在'.format(DBName))
spiders = client[DBName]
# 读取spiders数据库中的所有集合
print('list_collection_names: {}'.format(spiders.list_collection_names()))
# 声明一个student集合对象
spiders['student'].drop()
student = spiders['student']
record = {'_id': '20170101', 'name': 'Vector', 'age': 30, 'gender': 'male'}
result = student.insert_one(record)
record = [{'_id': '20170102', 'name': 'Jordan', 'age': 20, 'gender': 'male'},
          {'_id': '20170203', 'name': 'Mike', 'age': 21, 'gender': 'male'}]
student.insert_many(record)
print('Total: {}\n'.format(student.estimated_document_count()))

results = student.find({'name': 'Vector'}).sort('name', ASCENDING)
for result in results:
    print(result.get('_id'))
print()
results = student.find({'age': {'$gt': 18}}).skip(1).limit(2)
for result in results:
    print(result)
print()
record = student.find_one({'_id': '20170102'})
print(record)
result = student.update_one({'_id': '20170203'}, {'$set': {'name': 123, 'age': '60'}})
print('成功更新{}条记录'.format(result.modified_count))
result = student.delete_one({'name': 'vector'})
print('成功删除{}条记录'.format(result.deleted_count))
print('Total: {}'.format(student.estimated_document_count()))

# import pymysql

# db = pymysql.connect(host='localhost', port=3306,
#                      user='root', password='root')
# cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('Database version:', data)

# # 执行sql语句创建数据库spiders
# cursor.execute("CREATE DATABASE spiders DEFAULT CHARACTER SET utf8")
# # 执行sql语句指定要操作的数据库
# cursor.execute('USE spiders')
# # 执行sql语句创建student表
# sql = 'CREATE TABLE IF NOT EXISTS student (id VARCHAR(255) NOT NULL,\
#        name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
# cursor.execute(sql)
# # 执行sql语句插入一条学生记录
# sql1 = 'INSERT INTO student(id, name, age) values(%s, %s, %s)'
# data = {'id': '20120002', 'name': 'Vector', 'age': 30}
# sql2 = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(
#     table='student',
#     keys=', '.join(data.keys()),
#     values=', '.join(['%s'] * len(data)))

# try:
#     cursor.execute(sql1, ('20120001', 'Bob', 20))
#     cursor.execute(sql2, tuple(data.values()))
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()

# try:
#     cursor.execute('SELECT * FROM student')
#     print('Count:', cursor.rowcount)
#     row = cursor.fetchone()
#     # rows = cursor.fetchall()
#     while row:
#         print('Row:', row)
#         row = cursor.fetchone()
# except Exception as e:
#     print(e)
# db.close()

# import csv
# import pandas as pd

# # 写入CSV文件
# with open('code/data.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     writer = csv.DictWriter(csvfile,
#                             fieldnames=['id', 'name', 'age'],
#                             delimiter='-')
#     writer.writeheader()
#     writer.writerow({'id': '10005', 'name': '王伟', 'age': 22})
#     writer = csv.writer(csvfile, delimiter='-')
#     writer.writerow(['10001', 'Mike', 20])
#     writer.writerow(['10002', 'Bob', 22])
#     writer.writerow(['10003', 'Jordan', 21])

# # 读取CSV文件
# with open('data.csv', 'r', encoding='utf-8') as csvfile:
#     reader = csv.reader(csvfile)
#     for row in reader:
#         print(row)

# df = pd.read_csv('data.csv')
# print(df)

# import json

# # Json字符串的读取
# str = '''
# [
#   {
#     "name": "鲍勃",
#     "gender": "男",
#     "birthday": "1992-10-18"
#   }, {
#     "name": "莉娜",
#     "gender": "女",
#     "birthday": "1995-10-18"
#   }
# ]
# '''
# print(json.loads(str))

# # 数据存储为Json文件
# with open('code/data.json', 'w+', encoding='utf-8') as file:
#     file.write(json.dumps(str))

# # Json文件的读取
# with open('code/data.json', 'r') as file:
#     str = file.read()
#     print(json.loads(str))

# import requests
# from lxml import etree
# from requests import RequestException
# from requests import cookies

# def saveHTMLPage(name, url, header, jar):
#     try:
#         response = requests.get(url, header, cookies=jar)
#         if response.status_code == 200:
#             with open(name, mode='w+', encoding='utf-8') as f:
#                 f.write(response.text)
#         else:
#             print(response.reason)
#     except RequestException as e:
#         print(e.reason)

# def parseHTMLPage(pattern, name):
#     html = etree.parse(name, etree.HTMLParser())
#     return html.xpath(pattern)

# if __name__ == '__main__':
#     jar = requests.cookies.RequestsCookieJar()
#     header = {
#         'User-Agent':
#         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
#     }
#     saveHTMLPage('code/zhihu1.html', 'https://www.zhihu.com/explore', header)
