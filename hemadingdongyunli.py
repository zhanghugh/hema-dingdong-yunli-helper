#!/usr/bin/python
# -*- coding: UTF-8 -*-
#python3
#nodejs

import requests
import json
import time
import execjs
import copy

timenow = str(int(time.time()))
#timenow = '1650413974' #测试用

#盒马请求网页，挑选一个一直有货的商品推荐贵的酒类

hemaurl = ' '

#叮咚请求参数，按抓包填入header
#获取https://trackercollect.ddxq.mobi/appInfo/bundle 中的request信息
#通过网页解码encodeURIComponent http://tools.jb51.net/transcoding/urlencode_decode

city_number = '0101'
app_version = '2.83.1'
address_id = ''
station_id = ''
app_client_id = '4'
longitude = '' #ddmc-longitude
latitude = '' #ddmc-latitude
api_version = '9.50.0'
uid = '' #ddmc-uid

#叮咚请求参数，按抓包填入data

s_id = ''
openid = ''
device_token = ''

products = ''' '''


#命令开始

urldingdong='https://maicai.api.ddxq.mobi/order/getMultiReserveTime'
urldingdong2='https://maicai.api.ddxq.mobi/cart/index'

headerdingdong = {
    'content-type': 'application/x-www-form-urlencoded',
    'ddmc-city-number': city_number,
    'ddmc-longitude': longitude,
    'ddmc-latitude': latitude,
    'ddmc-build-version': app_version,
    'ddmc-device-id': openid,
    'ddmc-station-id': station_id,
    'ddmc-channel': 'applet',
    'ddmc-os-version': '[object Undefined]',
    'ddmc-app-client-id': app_client_id,
    'ddmc-api-version': api_version,
    'ddmc-uid': uid,
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B93 MicroMessenger/8.0.10(0x18000a2a) NetType/WIFI Language/zh_CN',
    'accept-encoding': 'gzip,compress,br,deflate',
    'ddmc-time':timenow,
    'cookie': 'DDXQSESSID='+s_id,
    'referer': 'https://servicewechat.com/wx1e113254eda17715/432/page-frame.html',
}

hemaheader = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'sec-ch-ua-platform':'"macOS"',
    'sec-ch-ua':'" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
    "Cache-Control": "no-cache",
    'pragma': 'no-cache',
    'referer': 'https://hema.taobao.com/s/itemdetail?shopid=198914196&serviceid=605102801030',
    'authority': 'h5api.m.taobao.com',
}

cookie={'DDXQSESSID': s_id}

signjsondata={
    'uid': uid,
    'longitude': longitude,
    'latitude': latitude,
    'station_id': station_id,
    'city_number': city_number,
    'api_version': api_version,
    'applet_source': '',
    'channel': 'applet',
    'app_client_id': app_client_id,
    'app_version': app_version,
    'sharer_uid': '',
    's_id': s_id,
    'openid': openid,
    'h5_source': '',
    'time': timenow,
    'device_token': device_token,
    'address_id': address_id,
    'group_config_id':'',
    'products': products,
    'isBridge': 'false',
}

cartjsondata={
    'uid': uid,
    'longitude': longitude,
    'latitude': latitude,
    'station_id': station_id,
    'city_number': city_number,
    'api_version': api_version,
    'applet_source': '',
    'channel': 'applet',
    'app_client_id': app_client_id,
    'app_version': app_version,
    'sharer_uid': '',
    's_id': s_id,
    'openid': openid,
    'h5_source': '',
    'time': timenow,
    'device_token': device_token,
    'is_load': '1',
    'ab_config': '''{"key_onion":"D","key_cart_discount_price":"C"}''',
}
requestjsondata = copy.deepcopy(signjsondata)
getjsondata = copy.deepcopy(cartjsondata)

with open('sign.js', 'r', encoding='UTF-8') as f:
    signjs_code = f.read()
contextjs = execjs.compile(signjs_code)


for i in range(800): #循环800次

    hemahtmls = session.get(hemaurl, headers=hemaheader)
    hemahtmls.html.render(sleep=12) # js渲染
    hemapages = hemahtmls.html.text
    print(hemapages)
    if '配送小哥已约满' in hemapages:
        print('盒马无运力')
    else:
        if '现在下单' in hemapages:
            #requests.get('https://api2.pushdeer.com/message/push?pushkey= &text=盒马可下单') #推送到手机可选
            print('盒马有运力')
        else:
            #requests.get('https://api2.pushdeer.com/message/push?pushkey= &text=盒马错误')  # 推送到手机可选
            print('盒马错误')

    headerdingdong['time'] = signjsondata['time'] = requestjsondata['time'] = getjsondata['time'] = cartjsondata['time'] = str(int(time.time())) #更新time字段

    # 生成更新nars&sesi

    signjsondatajs = json.dumps(signjsondata)
    cartjsondatajs = json.dumps(cartjsondata)

    #sign运算
    signnarsout = contextjs.call("sign",signjsondatajs)
    signnarsout = json.loads(signnarsout)
    #print(signnarsout) #测试用

    requestjsondata['nars'] = signnarsout['nars']
    requestjsondata['sesi'] = signnarsout['sesi']

    #cart运算
    cartnarsout = contextjs.call("sign",cartjsondatajs)
    cartnarsout = json.loads(cartnarsout)
    #print(cartnarsout) #测试用

    getjsondata['nars'] = cartnarsout['nars']
    getjsondata['sesi'] = cartnarsout['sesi']


    htmldingdong = requests.post(urldingdong, headers=headerdingdong, data=requestjsondata, cookies=cookie)
    htmlsdingdong = htmldingdong.text
    print(htmlsdingdong)

    htmldingdong2 = requests.get(urldingdong2, headers=headerdingdong, params=getjsondata, cookies=cookie)
    htmlsdingdong2 = htmldingdong2.text
    print(htmlsdingdong2)

    if '"disableMsg":null' in htmlsdingdong:

        print('叮咚有运力')

        if '自动尝试可用时段' in htmlsdingdong:
            print('叮咚即将开放运力')
            #requests.get('https://api2.pushdeer.com/message/push?pushkey= &text=叮咚即将开放运力')  # 推送到手机可选

        else:
            for ii in range(15):  # 如果查询失败将循环15次
                if '当前人多拥挤' in htmlsdingdong2:
                    print('叮咚拥挤')
                    time.sleep(1)
                else:

                    if 'total_origin_money' in htmlsdingdong2:

                        print('叮咚有货有运力')
                        #requests.get('https://api2.pushdeer.com/message/push?pushkey= &text=叮咚有货有运力')# 推送到手机可选
                        break
                    else:

                        print('部分无货有运力')
                        #requests.get('https://api2.pushdeer.com/message/push?pushkey= &text=叮咚部分无货有运力')# 推送到手机可选
                        break
    else:
        if '已约满' in htmlsdingdong:
            print('叮咚无运力')
        else:
            #requests.get('https://api2.pushdeer.com/message/push?pushkey= &text=叮咚错误')
            print('叮咚错误')

    time.sleep(80)






