from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def sousuo(word):
    drive.find_element_by_css_selector('#key').send_keys(word)
    drive.find_element_by_css_selector('#search > div > div.form > button').click()


    drive.implicitly_wait(10) #渲染数据
    drive.maximize_window() #最大化浏览器

def drop_down():
    for x in range(1,21,1):
        time.sleep(0.5)
        j = x / 10 #按照分数位滑动距离
        js = "document.documentElement.scrollTop=document.documentElement.scrollHeight * %s"% j #头部到底部
        drive.execute_script(js)

def data():
    lis = drive.find_elements_by_css_selector('.gl-item')
    for li in lis:
        name = li.find_element_by_css_selector('div.p-name a em').text
        name=name.replace('京东超市','').replace('"','').replace('\n','')
        jiage = li.find_element_by_css_selector('div.p-price  strong i').text+"元"
        # name = li.find_element_by_css_selector('div.p-name a em').text
        print(name,jiage,sep='|')

def next():
    drive.find_element_by_css_selector('#J_bottomPage > span.p-num > a.pn-next > em').click()

    # 进入到下一页




keyword=input("请输入你要搜索的商品:")
#实例化浏览器对象

# keyword=input('请输入：')
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.binary_location = (r'C:\Users\马荣鑫\AppData\Local\Google\Chrome\Application\chrome.exe')  # 谷歌安装路径
# drive=webdriver.Chrome(executable_path='D:/DcBrowserDownloads/chromedriver_win32 (2)/chromedriver.exe') #添加依赖
# drive = webdriver.Chrome(executable_path='D:/DcBrowserDownloads/chromedriver_win32 (2)/chromedriver.exe',options=chrome_options)
s = Service(r"D:/DcBrowserDownloads/chromedriver_win32 (2)/chromedriver.exe")
drive = webdriver.Chrome(service=s)
drive.get("https://www.jd.com") #获取网址

sousuo(keyword)
if __name__ == '__main__':
    # chrome_options = Options()
    # chrome_options.add_argument('--ignore-certificate-errors')
    # chrome_options.add_argument('--headless')
    # chrome_options.add_argument('--disable-gpu')
    # chrome_options.binary_location = (r'C:\Users\马荣鑫\AppData\Local\Google\Chrome\Application\chrome.exe')  # 谷歌安装路径

    # driver = webdriver.Chrome(executable_path='D:/DcBrowserDownloads/chromedriver_win32 (2)/chromedriver.exe',
                              # options=chrome_options)

    for page in range(1,10): #循环10页
        next()
        drop_down()
        data()
    input() #退出
    drive.quit()


