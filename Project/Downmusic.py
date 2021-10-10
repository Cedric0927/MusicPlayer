
from selenium import webdriver
import os
from urllib.request import urlretrieve
import urllib
song_name = ''



def get_music_name(name):
    #获取用户搜索的歌名
    # name = entry.get()
    url = 'https://music.163.com/#/search/m/?s={}&type1'.format(name)
    chromedriverpath = "chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriverpath
    # 隐藏浏览器
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    driver = webdriver.Chrome(chromedriverpath, options=option)
    # 显示浏览器
    # options = webdriver.ChromeOptions()
    # prefs = {"download.default_directory": r"D:\New_Download"}
    # options.add_experimental_option("prefs", prefs)
    # print(options.experimental_options)
    # chromeDriverPath = r'D:\\chromedriver.exe'
    # driver = webdriver.Chrome(chromeDriverPath, chrome_options=options)


    # 搜索歌曲页面
    # driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    driver.switch_to.frame('g_iframe')
    # 获取id
    req = driver.find_element_by_id('m-search')
    a_id = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute('href')
    print(a_id)
    song_id = a_id.split('=')[-1]
    print(song_id)

    # 获取歌曲名
    global song_name
    song_name = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//b').get_attribute('title')
    print(song_name)
    # 构造字典
    item = {'song_id': song_id, 'song_name': song_name}
    # 退出
    driver.quit()
    song_load(item)


def song_load(item):
    song_id = item['song_id']

    song_name = item['song_name']

    song_url = r'http://music.163.com/song/media/outer/url?id={}.mp3'.format(song_id)

    # 创建文件夹
    # os.makedirs('music_netease', exist_ok=True)
    path = r'D:\Graduation_Project\Music\{}.mp3'.format(song_name)

    # 显示数据到文本框

    # text.insert(END, '歌曲：{},正在下载…'.format(song_name))
    # # 文本框滚动
    # text.see(END)
    # # 更新
    # text.update()
    #下载
    opener = urllib.request.build_opener()
    headers = {
        'Referer': 'https://music.163.com/',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 "
                      "Safari/537.36"
    }
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
    urlretrieve(song_url, path)
    # #
    # text.insert(END, '下载完毕：{}请试听'.format(song_name))
    # text.see(END)
    # text.update()


# 界面
# root = Tk()
# root.title('音乐')
# root.geometry('560x450+400+200')
#
# label = Label(root, text='请输入下载的音乐： ', font=('华文行楷', 20))
# label.grid()
#
# entry = Entry(root, font=('隶书', 20))
# entry.grid(row=0, column=1)
#
# text = Listbox(root, font=('楷书', 16), width=50, height=15)
# text.grid(row=1, columnspan=2)
#
# button = Button(root, text='开始下载', font=('楷书', 15), command=get_music_name)
# button.grid(row=2, column=0, sticky=W)
# button1 = Button(root, text='退出程序', font=('楷书', 15), command=root.quit)
# button1.grid(row=2, column=1, sticky=E)
#
# root.mainloop()
#
