import requests
import execjs
from bs4 import BeautifulSoup
import re
from urllib import parse

if __name__ == '__main__':
    url='http://ac.scmor.com/'
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    html=requests.get(url,headers=headers).text
    soup=BeautifulSoup(html,'lxml')
    infs=soup.find('head').find_all('script',type='text/javascript')
    infs=re.findall(r'autourl(.*?);',str(infs))
    node = execjs.get()
    file = '谷歌学术镜像.js'
    ctx = node.compile(open(file, encoding='utf-8').read())
    for inf in infs:
        data=inf.split('=',1)[1][2:-1]
        js='strdecode("{}") '.format(data)
        print(ctx.eval(js))
        print(data)
'''


data={'i': '与', 'from': 'AUTO', 'to': 'AUTO', 'smartresult': 'dict', 'client': 'fanyideskweb', 'ts': '1545184610610', 'salt': '1545184610612', 'sign': '70131906b5948921e708440b9387cda6', 'bv': 'b34b626f1c1da1753c455d5223882b69', 'doctype': 'json', 'version': '2.1', 'keyform': 'fanyi.web', 'action': 'FY_BY_CLICKBUTTION', 'typoResult': 'false'}
data={
'i': '翻译',
'from': 'AUTO',
'to': 'AUTO',
'smartresult': 'dict',
'client': 'fanyideskweb',
'salt': '15451840702190',
'sign': 'c09462d9c1f2736f9a77fb3ac77f60ee',
'ts': '1545184070219',
'bv': 'b34b626f1c1da1753c455d5223882b69',
'doctype': 'json',
'version': '2.1',
'keyfrom': 'fanyi.web',
'action': 'FY_BY_REALTIME',
'typoResult': 'false'}
print(parse.urlencode('fanyideskweb'))
headers = {
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection': 'keep-alive',
#'Content-Length': str(len(data)),
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'Cookie': 'OUTFOX_SEARCH_USER_ID=-885057027@10.168.8.76; OUTFOX_SEARCH_USER_ID_NCOO=732654672.7229686; JSESSIONID=aaaxqlJYLuXkMcyMejeFw; ___rl__test__cookies=1545184070216',
'Host': 'fanyi.youdao.com',
'Origin': 'http://fanyi.youdao.com',
'Referer': 'http://fanyi.youdao.com/',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest'}
print(len(data))
url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
html=requests.post(url,data=data,headers=headers)
print(html.text)
data={
'i': '翻译',
'from': 'AUTO',
'to': 'AUTO',
'smartresult': 'dict',
'client': 'fanyideskweb',
'salt': '15451840702190',
'sign': 'c09462d9c1f2736f9a77fb3ac77f60ee',
'ts': '1545184070219',
'bv': 'b34b626f1c1da1753c455d5223882b69',
'doctype': 'json',
'version': '2.1',
'keyfrom': 'fanyi.web',
'action': 'FY_BY_REALTIME',
'typoResult': 'false'}

'''