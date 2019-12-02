from lxml import etree
from urllib import request
import time
import threading
import pandas
start = time.time()
housedetail=[]
class One(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):

        url="https://m.lianjia.com/sh/xiaoqu/"
        headers = {'Referer': url,
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko',
                        'Cookie':'admckid=1910211642301346651'}
        req = request.Request(url, headers=headers)
        html = request.urlopen(req).read().decode('utf-8')
        html = etree.HTML(html)
        links = html.xpath('//ul[@class="level2 active"]/li/a/@href')[1:-1]
        area = html.xpath('//ul[@class="level2 active"]/li/a/text()')[1:-1]
        for area,link in zip(area,links):
            for n in range(1,5,2):
                try:
                    start1 = time.time()
                    print('线程1··正在爬取'+area+'~~第'+str(n)+'页·····')
                    url = "https://m.lianjia.com/sh/xiaoqu/pg" + str(n) + "/"
                    headers = {'Referer': url,
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko'}
                    req = request.Request(url, headers=headers)
                    html = request.urlopen(req).read().decode('utf-8')
                    html = etree.HTML(html)
                    #print(html)
                    links = html.xpath('//li[@class="pictext"]/a/@href')
                    print(links)
                    for i in links:
                        result = {}
                        #print(i)
                        result['area']=area
                        req = request.Request(i, headers=headers)
                        html = request.urlopen(req).read().decode('utf-8')
                        html = etree.HTML(html)
                        result['name'] = html.xpath('//div[@class="xiaoqu_head_title lazyload_ulog"]/h1/text()')[0]
                        # print(result['name'])
                        result['address'] = html.xpath('//div[@class="xiaoqu_head_title lazyload_ulog"]/p[@class="xiaoqu_basic"]/span/text()')[0]
                        # print(result['address'])
                        result['price'] = html.xpath('//div[@class="xiaoqu_price"]/p/span/text()')[0]
                        # print(result['price'])
                        # a = html.xpath('//p[@class="text_cut"]/span[@class="sub_title"]/text()')[0]
                        # b = html.xpath('//p[@class="text_cut"]/em/text()')[0]
                        # result['jianzhu'] = str(a) + str(b)
                        result['jianzhuniandai']=html.xpath('//div[@class="worth_card"]/div[@class="worth_guide"]/ul/li/text()')[1]
                        result['fangwuzongshu'] = html.xpath('//div[@class="worth_card"]/div[@class="worth_guide"]/ul/li/text()')[2]
                        result['loudongzongshu'] = html.xpath('//div[@class="worth_card"]/div[@class="worth_guide"]/ul/li/text()')[3]

                        result['link'] = i
                        #print(result)
                        housedetail.append(result)
                        # print(housedetail)

                except:
                    pass
                print('爬取' + area + '第' + str(n) + '页完成,用时:', time.time() - start1)
        df = pandas.DataFrame(housedetail)
        df.columns = ['adress', 'area', 'link', 'name', 'jianzhuniandai','fangwuzongshu','loudongzongshu','price']
        df.to_csv('housedata1.csv', mode='a', encoding='gbk', header=False, index=False)
        elapsed = (time.time() - start)
        print("Time used:",elapsed)
housedetail1=[]
class Two(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):

        url="https://m.lianjia.com/sh/xiaoqu/"
        headers = {'Referer': url,
                       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko'}
        req = request.Request(url, headers=headers)
        html = request.urlopen(req).read().decode('utf-8')
        html = etree.HTML(html)
        links = html.xpath('//ul[@class="level2 active"]/li/a/@href')[1:-1]
        area = html.xpath('//ul[@class="level2 active"]/li/a/text()')[1:-1]
        for area,link in zip(area,links):
            for n in range(2,5,2):
                try:
                    start2=time.time()
                    print('线程2---正在爬取'+area+'~~第'+str(n)+'页---')
                    url = "https://m.lianjia.com/sh/xiaoqu/pg" + str(n) + "/"
                    headers = {'Referer': url,
                           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko'}
                    req = request.Request(url, headers=headers)
                    html = request.urlopen(req).read().decode('utf-8')
                    html = etree.HTML(html)
                    #print(html)
                    links = html.xpath('//li[@class="pictext"]/a/@href')
                    #print(links)
                    for i in links:
                        result = {}
                        #print(i)
                        result['area']=area
                        req = request.Request(i, headers=headers)
                        html = request.urlopen(req).read().decode('utf-8')
                        html = etree.HTML(html)
                        result['name'] = html.xpath('//div[@class="xiaoqu_head_title lazyload_ulog"]/h1/text()')[0]
                        # print(result['name'])
                        result['address'] = html.xpath('//div[@class="xiaoqu_head_title lazyload_ulog"]/p[@class="xiaoqu_basic"]/span/text()')[0]
                        # print(result['address'])
                        result['price'] = html.xpath('//div[@class="xiaoqu_price"]/p/span/text()')[0]
                        result['jianzhuniandai']=html.xpath('//div[@class="worth_card"]/div[@class="worth_guide"]/ul/li/text()')[1]
                        result['fangwuzongshu'] = html.xpath('//div[@class="worth_card"]/div[@class="worth_guide"]/ul/li/text()')[2]
                        result['loudongzongshu'] = html.xpath('//div[@class="worth_card"]/div[@class="worth_guide"]/ul/li/text()')[3]

                        result['link'] = i
                        #print(result)
                        housedetail1.append(result)
                        # print(housedetail)

                except:
                    pass
                print('爬取' + area + '第' + str(n) + '页完成,用时:', time.time() - start2)
        df = pandas.DataFrame(housedetail1)
        df.columns = ['adress', 'area', 'link', 'name', 'jianzhuniandai','fangwuzongshu','loudongzongshu','price']
        df.to_csv('housedata2.csv', mode='a', encoding='gbk', header=False, index=False)
        elapsed = (time.time() - start)
        print("Time used:",elapsed)

one=One()
one.start()
two=Two()
two.start()