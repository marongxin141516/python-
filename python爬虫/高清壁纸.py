from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
import requests
import parsel
import time
from  lxml import etree

# import requests
# from lxml import etree
# url = 'https://wallhaven.cc/search?q=id%3A65348&sorting=random&ref=fp&seed=Y86zuK&page=15'
# # url = 'https://wallhaven.cc/w/x8l9jz'
#
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
#
# }
# response = requests.get(url,headers=headers)
# # print(response.text)
# sel = etree.HTML(response.text)
# datas = sel.xpath('//*[@id="thumbs"]/section[1]/ul/li')
# for data in datas:
#     dizhiurl = data.xpath('figure/a/@href')
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
#         'referer': str(dizhiurl)
#         }
    # response1 = requests.get(dizhiurl, headers=headers)
    # sel1 = etree.HTML(response1.text)
    # img = sel1.xpath('//*[@id="wallpaper"]')

    # print(dizhiurl)


def download(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
    response=requests.get(url,headers=headers)
    # decode=response.content.decode('utf-8')
    set=response.text
    list=parsel.Selector(set)
    data=list.xpath('//*[@id="thumbs"]/section/ul/li/figure/a/@href').getall()

    for xinurl in data:
        # xurl='http://pic.netbian.com'+i
        # print(xinurl)

        time.sleep(3)
        response1 = requests.get(url=xinurl, headers=headers)
        #
        set1 = response1.text
        list1 = parsel.Selector(set1)
        data1= list1.xpath('//*[@id="wallpaper"]/@src').get()
        # img_url = 'http://pic.netbian.com' + data1
        # print(data1)




        # if data1:
        # #
        img_data = requests.get(data1, headers=headers).content  # content取出二进制数据，图片都是二进制数据
        #
        file_name = data1.split('/')[-1]
        # print(file_name)
        # #
        with open('高清壁纸\\' + file_name, 'wb') as f:
            print('正在保存图片：', file_name)
            f.write(img_data)

if __name__ == '__main__':
    # with ThreadPoolExecutor(40) as t: #创建线程池
    #     for i in range(2,10):
    #         t.submit(download,f'https://wallhaven.cc/toplist?page={i}')#将任务提交给线程池，由线程池分布任务
    for i in range(1,5):
        download('https://wallhaven.cc/toplist?page={i}')