import execjs
import requests

def translate(key,fro,to):
    node = execjs.get()
    file = '百度翻译.js'
    ctx = node.compile(open(file, encoding='utf-8').read())
    token,u=parame()
    js = 'e("{0}","{1}")'.format(key,u)
    sign = ctx.eval(js)
    print(sign)
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'BIDUPSID=A0BE57EF0645F17DEC806F36F3E38844; PSTM=1531234350; BAIDUID=EEEDF0D3A7636804D4AF070CB10CC56A:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=VUTVlhSTlOdnhnN3pRRlNBdU0tT21KMnBUMUlJS3Z0ZlJRMzd5MlVVQU1zdmRiQVFBQUFBJCQAAAAAAAAAAAEAAAAl6sYTz8TM7LXEzqLQpk5WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwl0FsMJdBbZz; MCITY=-315%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1442_21095_28132_26350_27751_27244_27509; delPer=0; PSINO=1; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1545304167; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1545307350; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D',
            'Host': 'fanyi.baidu.com',
        'Origin': 'https://fanyi.baidu.com',
        'Referer': 'https://fanyi.baidu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    data = {
        'from': fro,
        'to':to,
        'query': key,
        'transtype': 'translang',
        'simple_means_flag': '3',
        'sign': sign,
        #'token':'04a7c540f2a1e1d6be3dee208d1b7525'
        'token':token[1:-1]
    }
    url = 'https://fanyi.baidu.com/v2transapi'
    html = requests.post(url, data=data, headers=headers).json()
    html=html['trans_result']['data'][0]
    result={
        html['src']:html['dst']
    }
    print(result)
    return result
import re
def parame():
    url = 'https://fanyi.baidu.com/?aldtype=16047'
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'BIDUPSID=A0BE57EF0645F17DEC806F36F3E38844; PSTM=1531234350; BAIDUID=EEEDF0D3A7636804D4AF070CB10CC56A:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=VUTVlhSTlOdnhnN3pRRlNBdU0tT21KMnBUMUlJS3Z0ZlJRMzd5MlVVQU1zdmRiQVFBQUFBJCQAAAAAAAAAAAEAAAAl6sYTz8TM7LXEzqLQpk5WAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwl0FsMJdBbZz; MCITY=-315%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1442_21095_28132_26350_27751_27244_27509; delPer=0; PSINO=1; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1545304167; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1545305626; from_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D',
        'Host': 'fanyi.baidu.com',
        'Origin': 'https://fanyi.baidu.com',
        'Referer': 'https://fanyi.baidu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    html = requests.get(url,headers=headers).text
    windows_gtk = re.findall(r';window.gtk = (.*?);</script>', html)[0][1:-1]
    window_bdstoken = re.findall(r'<script>window.bdstoken = (.*?);window.gtk', html)[0]
    token = re.findall(r"token: (.*?),", html)[0]
    logid = re.findall(r'logid: (.*?),', html)[0][1:-1]
    #print(window_bdstoken, windows_gtk, token, logid)
    return token,windows_gtk
if __name__ == '__main__':
    #key=input('请输入要翻译的文字')
    dic = {'中文': 'zh', '日语': 'jp', '日语假名': 'jpka', '泰语': 'th', '法语': 'fra', '英语': 'en', '西班牙语': 'spa', '韩语': 'kor',
           '土耳其语': 'tr', '越南语': 'vie', '马来语': 'ms', '德语': 'de', '俄语': 'ru', '伊朗语': 'ir', '阿拉伯语': 'ara', '爱沙尼亚语': 'est',
           '白俄罗斯语': 'be', '保加利亚语': 'bul', '印地语': 'hi', '冰岛语': 'is', '波兰语': 'pl', '波斯语': 'fa', '丹麦语': 'dan',
           '菲律宾语': 'tl', '芬兰语': 'fin', '荷兰语': 'nl', '加泰罗尼亚语': 'ca', '捷克语': 'cs', '克罗地亚语': 'hr', '拉脱维亚语': 'lv',
           '立陶宛语': 'lt', '罗马尼亚语': 'rom', '南非语': 'af', '挪威语': 'no', '巴西语': 'pt_BR', '葡萄牙语': 'pt', '瑞典语': 'swe',
           '塞尔维亚语': 'sr', '世界语': 'eo', '斯洛伐克语': 'sk', '斯洛文尼亚语': 'slo', '斯瓦希里语': 'sw', '乌克兰语': 'uk', '希伯来语': 'iw',
           '希腊语': 'el', '匈牙利语': 'hu', '亚美尼亚语': 'hy', '意大利语': 'it', '印尼语': 'id', '阿尔巴尼亚语': 'sq', '阿姆哈拉语': 'am',
           '阿萨姆语': 'as', '阿塞拜疆语': 'az', '巴斯克语': 'eu', '孟加拉语': 'bn', '波斯尼亚语': 'bs', '加利西亚语': 'gl', '格鲁吉亚语': 'ka',
           '古吉拉特语': 'gu', '豪萨语': 'ha', '伊博语': 'ig', '因纽特语': 'iu', '爱尔兰语': 'ga', '祖鲁语': 'zu', '卡纳达语': 'kn', '哈萨克语': 'kk',
           '吉尔吉斯语': 'ky', '卢森堡语': 'lb', '马其顿语': 'mk', '马耳他语': 'mt', '毛利语': 'mi', '马拉提语': 'mr', '尼泊尔语': 'ne',
           '奥利亚语': 'or', '旁遮普语': 'pa', '凯楚亚语': 'qu', '塞茨瓦纳语': 'tn', '僧加罗语': 'si', '泰米尔语': 'ta', '塔塔尔语': 'tt',
           '泰卢固语': 'te', '乌尔都语': 'ur', '乌兹别克语': 'uz', '威尔士语': 'cy', '约鲁巴语': 'yo', '粤语': 'yue', '文言文': 'wyw',
           '中文繁体': 'cht'}
    key='为乐为魂之语与通〜'
    fro =dic['文言文']
    to=dic['英语']
    translate(key,fro,to)

