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
