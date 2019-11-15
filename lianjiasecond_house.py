import os
import pandas as pd
from selenium import webdriver
from pyquery import PyQuery as pq
driver = webdriver.Chrome()


'''
    步骤：
    1. 下载页面          
    2. 解析页面            
    3. 保存数据
'''


def cached_url(url):
    """
    缓存网页, 避免重复下载浪费时间
    """
    folder = 'cached'
    filename = url.split('/')[-2][2:] + '.html'   # 以页面数命名 html 页面
    path = os.path.join(folder, filename)
    if os.path.exists(path):
        with open(path, 'rb') as f:
            s = f.read()
            return s
    else:
        if not os.path.exists(folder):
            # 建立 cached 文件夹
            os.makedirs(folder)

        driver.get(url)    # 使用 Selenium 爬取页面
        with open(path, 'wb') as f:
            f.write(driver.page_source.encode())
        return driver.page_source


def house_from_div(div):
    """
    从一个 div 里面获取到一个二手房信息
    """
    e = pq(div)

    # 小作用域变量用单字符
    m = {}
    m['name'] = e('.houseInfo').text()  # 二手房名字
    m['price'] = e('.totalPrice').text()  # 二手房总价
    m['unitprice'] = e('.unitPrice').text()  # 二手房每平米单价
    m['position'] = e('.positionInfo').text()  # 二手房位置
    m['follow'] = e('.followInfo').text()  # 二手房关注信息
    m['url'] = e('a').attr('href')  # 二手房页面链接

    return m


def houses_from_url(url):
    """
    从 url 中下载网页并解析出页面内所有的房源
    """
    # 页面只需要下载一次
    page = cached_url(url)
    e = pq(page)
    items = e('.info.clear')  # 解析的class为info clear, 中间有空格, 使用“.info.clear”
    # 调用 house_from_div
    houses = [house_from_div(i) for i in items]
    return houses


def append_to_csv(data):
    '''
    保存数据
    '''
    file_name = './新房数据.csv'
    df = pd.DataFrame(data)
    df.to_csv(file_name, mode='a', encoding='gbk', header=False, index=False)


def main():
    for i in range(1, 101):
    # 一共 100 页房源信息
        url = 'https://sh.fang.lianjia.com/loupan/pg{}/'.format(i)
        houses = houses_from_url(url)
        print(houses)
        append_to_csv(houses)


if __name__ == '__main__':
    main()