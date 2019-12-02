from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

url = 'https://m.lianjia.com/nt/xiaoqu/'
headers = {'Referer': url,
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
           'Cookie': 'lianjia_uuid=443bb6e3-b556-47ea-967d-5444ea915dc6; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1571809948,1572075513,1572091757,1572092040; _smt_uid=5dafea9d.5470d44f; UM_distinctid=16df72c7718be-086f464eb904c-4c312373-144000-16df72c7719794; _jzqa=1.3017324979856383500.1571809949.1572094819.1572175751.7; _jzqy=1.1571809949.1572091757.1.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6.-; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216df72c7a34233-04d3d7bf7d75b18-4c312373-1327104-16df72c7a35214%22%2C%22%24device_id%22%3A%2216df72c7a34233-04d3d7bf7d75b18-4c312373-1327104-16df72c7a35214%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22sousuo%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; _ga=GA1.2.1379447899.1571809952; _jzqx=1.1571814886.1572175751.4.jzqsr=sh%2Elianjia%2Ecom|jzqct=/ershoufang/pg100/.jzqsr=nt%2Elianjia%2Ecom|jzqct=/xiaoqu/8745128002049017/; select_city=320600; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1572177857; _jzqc=1; _gid=GA1.2.487758797.1572075516; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiZjQ0ZDY4YmQzYWFiMTczNTkxNTgyYjBhNzkxMzc5N2I3ZTdmMjlhZTE2NzRlZTU4NjRlZjMyN2Q4MDVhZDdhMTRiOGJhNjNjMmEwYjNiZmIwMjI2ZGM5YWY5ZjQxMDA1MzkwYmJiMWFiMjBlYTJiNTkxMWY1ZmM4Y2ViYWRlOTg4NGQ5YjVhNWZhZTM2ZGRmMjJmZGQ3ZTAyMzUwNzM5NDc4OTNmMWQ3ZWM2ZWJkYzc1MjA2ZDRlZDE2YzA5MGQxYjVkZmRhNzNhYWI5NDMwYzUwYjIzNDI2ZmM5NTdkOTFjZTg0OTZhM2EzYzkwMmE5YzQwYjkxN2JlZWRlMmNmNzYxNGM0M2FlYTFlNjkyOGJkYzJhM2Q1M2ZhNmYxZTkyMjM0MjVmYTdmYTBhMGE4MTQ5NGI1MGY1Yjc5ZTJmNzMxNjUwMGE5NzdlMjZlMDA3YmU4Njg1NzliODQxNjIxZFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI2NmFmZjk1M1wifSIsInIiOiJodHRwczovL20ubGlhbmppYS5jb20vbnQveGlhb3F1LyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9; CNZZDATA1254525948=1706170696-1572075705-%7C1572172951; CNZZDATA1253491255=1450175482-1572074448-%7C1572172565; lianjia_ssid=91c55eb0-d2cf-7ad8-de18-58a73ecf6aab; _jzqckmp=1'}
page = ('pg')

# return demjson.encode(res)




def areainfo(url):
    page = ('pg')
    for i in range(1, 31):  # 获取1-100页的数据
        if i == 1:
            i = str(i)
            a = (url + page + i + '/')
            r = requests.get(url=a, headers=headers)
            print(a)
            htmlinfo = r.content
        else:
            i = str(i)
            a = (url + page + i + '/')
            print(a)
            r = requests.get(url=a, headers=headers)
            html2 = r.content
            htmlinfo = htmlinfo + html2
    time.sleep(0.5)
    return htmlinfo


hlist = []


def listinfo(listhtml):
    areasoup = BeautifulSoup(listhtml, 'html.parser')
    ljhouse = areasoup.find_all('a', attrs={'class': 'pictext'})

    for house in ljhouse:
        loupantitle = house.find("div", attrs={"class": "xiaoqu_head_title lazyload_ulog"})
        loupanname = loupantitle.a.get_text()
        # loupantag = loupantitle.find_all("span")
        # wuye = loupantag[0].get_text()
        # xiaoshouzhuangtai = loupantag[1].get_text()
        location = house.find("div", attrs={"class": "xiaoqu_head_address"}).get_text()
        a = house.find("div", attrs={"class": "mod_box jichuxinxi"})
        niandai=a.find("div", attrs={"class": "mod_cont"})[0].get_text()
        leixing=a.find("div", attrs={"class": "mod_cont"})[1].get_text()
        loudongshu=a.find("div", attrs={"class": "mod_cont"})[2].get_text()
        fangwushu=a.find("div", attrs={"class": "mod_cont"})[1].get_text()
        # price = house.find("div", attrs={"class": "main-price"}).get_text()
        # total = jiage.find("div", attrs={"class": "second"})
        # totalprice = "暂无"
        # if total is not None:
        #     totalprice = total.get_text()
        h = {'title': loupanname, 'location': location.replace("\n", ""),
             'niandai': niandai.replace("\n", ""), 'leixing': leixing, 'loudongshu': loudongshu, 'fangwushu': fangwushu};
        hlist.append(h)


if __name__ == '__main__':
    url = url
    hlist.append(
        {'title': "楼盘名称",  'location': "位置",
         'niandai': "建筑年代", 'leixing': "房屋类型", 'loudongshu': "楼栋数",
         'fangwushu': "房屋数"})
    areahtml = areainfo(url)
    listinfo(areahtml)
    # houseinfo = houseinfo.append(hlist)
    houseinfo = pd.DataFrame(hlist)
    houseinfo.to_csv('链家新房.csv', index=False, encoding="utf_8_sig")
