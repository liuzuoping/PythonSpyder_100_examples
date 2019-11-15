from aip import AipOcr
import pandas as pd
from sqlalchemy import create_engine
import os
import csv

def getsceenshot(search_url,list):
    from selenium import webdriver
    import os
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium import webdriver

    picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))

    try:
        File_Path = os.getcwd() + '\\' + directory_time + '\\'
        if not os.path.exists(File_Path):
            os.makedirs(File_Path)
            print("存入文件%s" % File_Path)
        else:
            print("写入新文件")
    except BaseException as msg:
        print("异常：%s" % msg)
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()

        js_height = "return document.body.clientHeight"

        # driver = webdriver.Chrome()
        driver.get(search_url)
        driver.execute_script("""
            (function () {
                $('.subnav-title').hide();
                $('.video-iframe').hide();
                $('.mouth-remak').hide();
                $('.contmain').hide();
                $('.footer_auto').hide();
                $('.mouth-title-end over-hid').hide();
                $('.user-cont').hide();
                $('.mouth-title-end').hide();
                $('.nav-typebar-g12').hide();
                $('.breadnav').hide();
                $('.minitop').hide();
                $('.topbar-header').hide();
                $('.gotop02').hide();
                $('.image-div').hide();
                $('.video-container').hide();
                $('.advbox1').hide();
                $('.mouthcon-cont-left').hide();
                $('.mouthcon-cont-right').attr('width','800');
                $('.text-con').attr('font-size','18');
                $('.img-list').hide();
            })();
        """)

        k = 1
        height = driver.execute_script(js_height)
        while True:
            if k * 500 < height:
                js_move = "window.scrollTo(0,{})".format(k * 500)
                print(js_move)
                driver.execute_script(js_move)
                time.sleep(0.2)
                height = driver.execute_script(js_height)
                k += 1
            else:
                break
        scroll_width = driver.execute_script('return document.body.parentNode.scrollWidth')
        scroll_height = driver.execute_script('return document.body.parentNode.scrollHeight')
        driver.set_window_size(scroll_width, scroll_height)
        driver.get_screenshot_as_file(
            '.\\' + directory_time + '\\' + picture_time + '.png')
        print("Process {} get one pic !!!".format(os.getpid()))
        list.append(search_url)
        print(list)


    except Exception as e:
        print(e)


    finally:
        driver.quit()
        print('爬取完成')
        return ('.\\' + directory_time + '\\' + picture_time + '.png')

def getlinks(links):
    list=[]
    for link in links:
        getsceenshot(link,list)
    df=pd.Series(list)
    df.to_csv('./lianjie.csv',index=False)

def getfile(rootdir):
    list = os.listdir(rootdir)#列出文件夹下所有的目录与文件
    lujing=[]
    for i in range(0,len(list)):
        rootdir = r'C:\Users\xiaoLiu\Desktop\11-10评论结果\2019-11-14'
        path = os.path.join(rootdir,list[i])
        lujing.append(path)
    df=pd.Series(lujing)
    df.to_csv('./pictureName.csv',index=False)

def get_file_content(filePath):
    """ 读取图片 """
    with open(filePath, 'rb') as fp:
        return fp.read()

def change_to_words(imgpath):
    APP_ID = '17523158'
    API_KEY = '9wyiqfr4Ob0llopVzzigi5T3'
    SECRET_KEY = 'Mo6Ctv7d6HstNesgPfiCOwxgeSw7nKyG'
    aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    for column in imgpath:
        options = {'detect_direction': 'true','language_type': 'CHN_ENG'}
        result = aipOcr.basicGeneral(get_file_content(column), options)
        words_result=result['words_result']
        list_result=str()
        for i in range(len(words_result)):
            list_result += words_result[i]['words']
        df=pd.Series(list_result)
        engine = create_engine("mysql+pymysql://root:960614abcd@localhost:3306/xiaoliu")
        df.to_sql(name = 'pinglun',con = engine,if_exists = 'append',index = False,index_label = False)

if __name__ == '__main__':
    df = pd.read_excel(r'C:\Users\xiaoLiu\Desktop\未处理链接.xlsx', header=0, index_col=None)
    links = df['字段4_link']
    getlinks(links)
    rootdir = r'C:\Users\xiaoLiu\Desktop\11-10评论结果\2019-11-14'
    getfile(rootdir)
    with open('./pictureName.csv','r',encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        imgpath = [row[0]for row in reader]
    change_to_words(imgpath)