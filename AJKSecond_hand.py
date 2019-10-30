import requests
import time
import csv
import random
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
    'Cookie':'sessid=F3A0D86E-9D3F-82F9-1BBA-D4A22CE6440F; aQQ_ajkguid=35DAB075-3352-357E-F3D9-D46F6E3E210A; lps=http%3A%2F%2Fwww.anjuke.com%2F%3Fpi%3DPZ-baidu-pc-all-biaoti%7Chttps%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00f7Hj1f0q3V-00PpAsK8poKI00000FYEi7C00000I5matL.THvs_oeHEtY0UWdVUv4_py4-g1PxuAT0T1d9PyPhPymLPW0sn1N-mW790ZRqwRuKfYFAPRwDfbRdrRPjfWKanWfsnYmsPYu7n1wKrHc0mHdL5iuVmv-b5HnzrHDvnH61njchTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8my4JIyV-QhPEUitOTAbqR7CVmh7GuZRVTAnVmyk_QyFGmyqYpfKWThnqPHRvP10%26tpl%3Dtpl_11534_19968_16032%26l%3D1514680221%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2-%2525E5%252585%2525A8%2525E6%252588%2525BF%2525E6%2525BA%252590%2525E7%2525BD%252591%2525EF%2525BC%25258C%2525E6%252596%2525B0%2525E6%252588%2525BF%252520%2525E4%2525BA%25258C%2525E6%252589%25258B%2525E6%252588%2525BF%252520%2525E6%25258C%252591%2525E5%2525A5%2525BD%2525E6%252588%2525BF%2525E4%2525B8%25258A%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2%2525EF%2525BC%252581%2526xp%253Did%28%252522m3291618302_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D129%26ie%3Dutf-8%26f%3D8%26tn%3Dmonline_3_dg%26wd%3D%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%26oq%3D%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%26rqlang%3Dcn; ctid=11; twe=2; _stat_guid=3050B320-8AA3-6F6A-9549-5BF2054466BB; _stat_rfpn=Ershou_Web_Property_List_FilterPage_tracklog; _prev_stat_guid=35DAB075-3352-357E-F3D9-D46F6E3E210A; 58tj_uuid=37c162b8-8162-4b45-aedf-dfa05080a10a; new_session=0; init_refer=https%253A%252F%252Fsp0.baidu.com%252F9q9JcDHa2gU2pMbgoY3K%252Fadrc.php%253Ft%253D06KL00c00f7Hj1f0q3V-00PpAsK8poKI00000FYEi7C00000I5matL.THvs_oeHEtY0UWdVUv4_py4-g1PxuAT0T1d9PyPhPymLPW0sn1N-mW790ZRqwRuKfYFAPRwDfbRdrRPjfWKanWfsnYmsPYu7n1wKrHc0mHdL5iuVmv-b5HnzrHDvnH61njchTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8my4JIyV-QhPEUitOTAbqR7CVmh7GuZRVTAnVmyk_QyFGmyqYpfKWThnqPHRvP10%2526tpl%253Dtpl_11534_19968_16032%2526l%253D1514680221%2526attach%253Dlocation%25253D%252526linkName%25253D%252525E6%252525A0%25252587%252525E5%25252587%25252586%252525E5%252525A4%252525B4%252525E9%25252583%252525A8-%252525E6%252525A0%25252587%252525E9%252525A2%25252598-%252525E4%252525B8%252525BB%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D%252525E5%252525AE%25252589%252525E5%252525B1%25252585%252525E5%252525AE%252525A2-%252525E5%25252585%252525A8%252525E6%25252588%252525BF%252525E6%252525BA%25252590%252525E7%252525BD%25252591%252525EF%252525BC%2525258C%252525E6%25252596%252525B0%252525E6%25252588%252525BF%25252520%252525E4%252525BA%2525258C%252525E6%25252589%2525258B%252525E6%25252588%252525BF%25252520%252525E6%2525258C%25252591%252525E5%252525A5%252525BD%252525E6%25252588%252525BF%252525E4%252525B8%2525258A%252525E5%252525AE%25252589%252525E5%252525B1%25252585%252525E5%252525AE%252525A2%252525EF%252525BC%25252581%252526xp%25253Did%28%25252522m3291618302_canvas%25252522%29%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FH2%2525255B1%2525255D%2525252FA%2525255B1%2525255D%252526linkType%25253D%252526checksum%25253D129%2526ie%253Dutf-8%2526f%253D8%2526tn%253Dmonline_3_dg%2526wd%253D%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2%2526oq%253D%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2%2526rqlang%253Dcn; new_uv=1; _ga=GA1.2.371539118.1571842678; _gid=GA1.2.389870108.1571842678; als=0; __xsptplus8=8.1.1571842677.1571846354.37%232%7Csp0.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%7C%23%23A8ZibGF0HQquvvworKFYDClvSKK6Plsf%23; isp=true; Hm_lvt_c5899c8768ebee272710c9c5f365a6d8=1571842689; Hm_lpvt_c5899c8768ebee272710c9c5f365a6d8=1571844621; __xsptplusUT_8=1; _gat=1'
}


def parse_pages(url, num):
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    result_list = soup.find_all('li', class_='list-item')
    # print(len(result_list))
    for result in result_list:
        # 标题
        title = result.find('a', class_='houseListTitle').text.strip()
        # print(title)
        # 户型
        layout = result.select('.details-item > span')[0].text
        # print(layout)
        # 面积
        cover = result.select('.details-item > span')[1].text
        # print(cover)
        # 楼层
        floor = result.select('.details-item > span')[2].text
        # print(floor)
        # 建造年份
        year = result.select('.details-item > span')[3].text
        # print(year)
        # 单价
        unit_price = result.find('span', class_='unit-price').text.strip()
        # print(unit_price)
        # 总价
        total_price = result.find('span', class_='price-det').text.strip()
        # print(total_price)
        # 关键字
        keyword = result.find('div', class_='tags-bottom').text.strip()
        # print(keyword)
        # 地址
        address = result.find('span', class_='comm-address').text.replace(' ', '').replace('\n', '')
        # print(address)
        # 详情页url
        details_url = result.find('a', class_='houseListTitle')['href']
        # print(details_url)
        results = [title, layout, cover, floor, year, unit_price, total_price, keyword, address, details_url]
        with open('anjuke.csv', 'a', newline='', encoding='utf-8-sig') as f:
            w = csv.writer(f)
            w.writerow(results)

    # 判断是否还有下一页
    next_url = soup.find_all('a', class_='aNxt')
    if len(next_url) != 0:
        num += 1
        print('第' + str(num) + '页数据爬取完毕！')
        # 3-60秒之间随机暂停
        time.sleep(random.randint(3, 60))
        parse_pages(next_url[0].attrs['href'], num)
    else:
        print('所有数据爬取完毕！')


if __name__ == '__main__':
    with open('anjuke.csv', 'a', newline='', encoding='utf-8-sig') as fp:
        writer = csv.writer(fp)
        writer.writerow(['标题', '户型', '面积', '楼层', '建造年份', '单价', '总价', '关键字', '地址', '详情页地址'])
    start_num = 0
    start_url = 'https://shanghai.anjuke.com/sale/'
    parse_pages(start_url, start_num)

