import requests
import csv
import random
import time
import socket
import http.client
from bs4 import BeautifulSoup
import re


def get_content(url, data=None):
    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'lianjia_uuid=8290c333-59db-490c-8808-8b2645f848c6; lianjia_ssid=55ca6233-79ad-4e5a-b366-831c546fe02e; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMjJmMmRhYzY2OTRjZTk2NDdjY2JlNDRiYTFhZTc1MDA0MjA3OTYwYTk2ZjlkZDE4MzFiYmJkZmEyNDc5MjhhZjU1NjZkYTJhMTU1NzkzNWU2M2IwYzY0ZjgzN2UwMDY4YzZiYTA3MWJkMzQ5MDc0MmI4NzU3YTY0MDhiNTFkMDc2MzhhNjI0MjI3YzBhNzk5YjYzYjg3MDE5ODM1ZjRlMWQ1ZDljNDBiMzczN2Q5MWQ1M2ZmMTQxYTZmNmE3MjQzNDBiZDk3YWI3MGVkMzdkM2FjYTQ3ZmViZjBmOWU1OTY3MDk1MmQ2OTgxMmQ4MmZkNjY5MzY5MjRhY2JmNTQwYzA3ZWMyMjA0MDBiNmQ5MDY5ZDZkYzQ2MTU2ODYwNTg1NjYxODljYTFkOTE3MDFlOWVkZTY2ZDllMWJiNjZlMGVmNmFmMGMyYjJkYThlNGFjYzhiNTY1YjY0NDFkNjhiYVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI3MzE0NjlkOVwifSIsInIiOiJodHRwczovL3NoLmxpYW5qaWEuY29tL3p1ZmFuZy8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    }
    timeout = random.choice(range(80, 180))
    while True:
        try:
            req = requests.get(url, headers=header, timeout=timeout)
            req.encoding = 'utf-8'
            break

        except socket.timeout as e:
            print('3:', e)
            time.sleep(random.choice(range(8, 15)))

        except socket.error as e:
            print('4:', e)
            time.sleep(random.choice(range(20, 60)))

        except http.client.BadStatusLine as e:
            print('5:', e)
            time.sleep(random.choice(range(30, 80)))

        except http.client.IncompleteRead as e:
            print('6:', e)
            time.sleep(random.choice(range(5, 15)))
    return req.text


def get_data(html_text):
    final = []
    bs = BeautifulSoup(html_text, "html.parser")
    body = bs.body
    data = body.find('div', {'id': 'content'}).find('div', {'class': 'content__article'})
    total = data.find('p', {'class': 'content__title'}).find('span', {'class': 'content__title--hl'}).string
    items = data.find('div', {'class': 'content__list'}).find_all('div', {'class': 'content__list--item'})

    for item in items:
        temp = []
        title = item.find('p', {'class': 'twoline'}).find('a').string
        price = str(item.find('span', {'class': 'content__list--item-price'}).text)
        infostr = str(item.find('p', {'class': 'content__list--item--des'}).text)
        try:
            type = str(item.find('p', {'class': 'content__list--item--brand'}).text)
        except:
            type = ''
        time = str(item.find('p', {'class': 'content__list--item--time'}).text)
        tag = str(item.find('p', {'class': 'content__list--item--bottom'}).text)
        title = re.sub(r'[\[\]\s]', '', title)
        infostr = re.sub(r'\s', '', infostr)
        info = infostr.split('/')
        type = re.sub(r'\s', '', type)
        tag = re.sub(r'\s', '', tag)
        address = info[0]
        size = info[1]
        fangxiang = info[2]
        format = info[3]
        # floor = info[4]
        temp.append(title)
        temp.append(price)
        temp.append(address)
        temp.append(size)
        temp.append(fangxiang)
        temp.append(format)
        # temp.append(floor)
        temp.append(type)
        temp.append(time)
        temp.append(tag)
        final.append(temp)
    return final


def write_data(data, name):
    file_name = name

    with open(file_name, 'a', errors='ignore', newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows([['title', 'price', 'address', 'size', 'fangxiang', 'format', 'type', 'time', 'tag']])
        f_csv.writerows(data)


if __name__ == '__main__':
    url = 'https://sh.lianjia.com/zufang/'
    # https://sh.lianjia.com/zufang/pujiang1/pg2rt200600000001l0/
    result = []
    for i in range(0, 99):
        html = get_content(url)
        d = get_data(html)
        result.extend(d)
        url = 'https://sh.lianjia.com/zufang/pg' + str(i+1) + '/#contentList'

    write_data(result, 'LJzufang.csv')