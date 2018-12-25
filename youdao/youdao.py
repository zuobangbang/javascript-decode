# -*- coding: utf-8 -*-
"""
Spyder Editor
zuobangbang
2018-12-25
This is a temporary script file.
"""

import requests
import time
import hashlib

def MD5(key):
    hash=hashlib.md5()
    hash.update(bytes(key,encoding='utf-8'))
    return hash.hexdigest()

def sign(key,salt):
    sign = "fanyideskweb" +key + str(salt) + "p09@Bn{h02_BIEe]$P^nG"
    return MD5(sign)
def translate(key):
    # url从http://fanyi.youdao.com输入词汇右键检查得到
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=true"

    salt = str(int(time.time()*1000)+random.randint(0,10))
    # data从右键检查FormData得到
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "ts":salt[:-1],
        "salt": salt,
        "sign": sign(key, salt),
        "bv":MD5("5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"),
        "doctype": "json",
        "version": "2.1",
        'keyfrom': 'fanyi.web',
'action': 'FY_BY_REALTIME',
'typoResult': 'false'}
    print(data)

    headers = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'OUTFOX_SEARCH_USER_ID=-885057027@10.168.8.76; OUTFOX_SEARCH_USER_ID_NCOO=732654672.7229686; JSESSIONID=aaaxqlJYLuXkMcyMejeFw; ___rl__test__cookies=1545184070216',
'Host': 'fanyi.youdao.com',
'Origin': 'http://fanyi.youdao.com',
'Referer': 'http://fanyi.youdao.com/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'}
    html=requests.post(url,data=data,headers=headers).json()
    print(html['translateResult'][0][0])

if __name__ == '__main__':
    translate("今天天气很好")
