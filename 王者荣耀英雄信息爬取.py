#-*- coding: UTF-8 -*-
from urllib.request import urlretrieve
import requests
import os


def hero_imgs_download(url, header):
    req = requests.get(url = url, headers = header).json()
    hero_num = len(req['list'])
    print('一共有%d个英雄' % hero_num)
    hero_images_path = 'hero_images'
    for each_hero in req['list']:
        hero_photo_url = each_hero['cover']
        hero_name = each_hero['name'] + '.jpg'
        filename = hero_images_path + '/' + hero_name
        if hero_images_path not in os.listdir():
            os.makedirs(hero_images_path)
        urlretrieve(url = hero_photo_url, filename = filename)


def hero_list(url, header):
	print('*' * 100)
	print('\t\t\t\t欢迎使用《王者荣耀》出装下助手！')
	print('*' * 100)
	req = requests.get(url = url, headers = header).json()
	flag = 0
	for each_hero in req['list']:
		flag += 1
		print('%s的ID为:%-7s' % (each_hero['name'], each_hero['hero_id']), end = '\t\t')
		if flag == 3:
			print('\n', end = '')
			flag = 0


def seek_weapon(equip_id, weapon_info):
	for each_weapon in weapon_info:
		if each_weapon['equip_id'] == str(equip_id):
			weapon_name = each_weapon['name']
			weapon_price = each_weapon['price']
			return weapon_name, weapon_price


def hero_info(url, header, weapon_info):
	req = requests.get(url = url, headers = header).json()
	print('\n历史上的%s:\n    %s' % (req['info']['name'], req['info']['history_intro']))
	for each_equip_choice in req['info']['equip_choice']:
		print('\n%s:\n   %s' % (each_equip_choice['title'], each_equip_choice['description']))
		total_price = 0
		flag = 0
		for each_weapon in each_equip_choice['list']:
			flag += 1
			weapon_name, weapon_price = seek_weapon(each_weapon['equip_id'], weapon_info)
			print('%s:%s' % (weapon_name, weapon_price), end = '\t')
			if flag == 3:
				print('\n', end = '')
				flag = 0
			total_price += int(weapon_price)
		print('神装套件价格共计:%d' % total_price)

def hero_weapon(url, header):
    req = requests.get(url = url, headers = header).json()
    weapon_info_dict = req['list']
    return weapon_info_dict


if __name__ == '__main__':
    headers = {'Accept-Charset': 'UTF-8',
            'Accept-Encoding': 'gzip,deflate',
            'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 5 MIUI/V8.1.6.0.MAACNDI)',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-type': 'application/x-www-form-urlencoded',
            'Connection': 'Keep-Alive',
            'Host': 'gamehelper.gm825.com'}
    weapon_url = "http://gamehelper.gm825.com/wzry/equip/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8"
    heros_url = "http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8"
    hero_list(heros_url, headers)
    hero_id = input("请输入要查询的英雄ID:")
    hero_url = "http://gamehelper.gm825.com/wzry/hero/detail?hero_id={}&channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8".format(hero_id)
    weapon_info_dict = hero_weapon(weapon_url, headers)
    hero_info(hero_url, headers, weapon_info_dict)