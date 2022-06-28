import requests
import parsel
from lxml import etree
import json
key = str(input('请输入歌手：'))
pn = int(input('输入几页：'))
url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}&rn=30'.format(key,pn)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Cookie": "kw_token=00P0ALXXZBXDO",
    "Referer": "http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6",
    "csrf": "00P0ALXXZBXDO" #跨站请求伪造
}
response=requests.get(url,headers=headers)

re = json.loads(response.text)
re1 = re["data"]["list"]
# print(re1)

for gequ in re1:
    name = gequ["name"]
    rid = gequ["rid"]
    name1 = str(name).split('-')[0]

    xinurl= 'http://www.kuwo.cn/api/v1/www/music/playUrl?mid='+str(rid)+'&type=musi&type=convert_url3&br=320kmp3'
    # xinurl = 'http://www.kuwo.cn/url?format=mp3&rid='+str(rid)+'&response=url&type=convert_url3&br=320kmp3'
    response1 = requests.get(url=xinurl, headers=headers)
    re2 = json.loads(response1.text)
    re3 = re2['data']['url']

    # print(name1)
    music = requests.get(re3, headers=headers).content
    with open('酷我\\' + name1 + '.mp3', 'wb') as f:
        print('正在下载：', name1)
        f.write(music)
    # try:
    #     with open('酷我音乐/{}.mp3'.format(name), 'wb')as f:
    #         print('正在下载{}'.format(name), end='')
    #         music = requests.get(re3)
    #         f.write(music.content)
    #         f.close()
    #         print('\t下载完成')
    # except:
    #     print('出现错误')
    


