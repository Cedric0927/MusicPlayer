import re
from selenium import webdriver
import time
import os
import importlib, sys

importlib.reload(sys)
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gbk')


def getSongSheet(url):
    print(url)
    html = getHTMLText(url)
    songmid = re.findall(r'https://y.qq.com/n/yqq/song/(.*?)(?=.html)', html, re.I | re.S | re.M)
    print(songmid)
    for i in songmid:
        print(i)
        songUrl = "https://y.qq.com/n/yqq/song/" + i + ".html"
        main(songUrl)
    print("全部完成")


def getHTMLText(url):
    chromedriverpath = "chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriverpath
    # 隐藏浏览器
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    driver = webdriver.Chrome(chromedriverpath, options=option)
    driver.get(url)
    time.sleep(3)
    return driver.page_source


def main(url):
    html = getHTMLText(url)
    html.encode("utf-8")
    html = html.encode("gbk", "ignore").decode("gbk")
    html.encode("utf-8")
    err = "很抱歉，您查看的歌曲已下架"
    if (err in html):
        return
    else:
        songname = re.findall(r'<h1 class="data__name_txt" .*?">(.*?)</h1>', html, re.I | re.S | re.M)
        singer = re.findall(
            r'<a.*?class="data__singer_txt js_singer" data-stat="y_new.song.header.singername" itemprop="byArtist">(.*?)</a>',
            html, re.I | re.S | re.M)
        liupai = re.findall(r'流派：(.*?)</li>', html,
                            re.I | re.S | re.M)
        yuzhong = re.findall(r'语种：(.*?)</li>', html, re.I | re.S | re.M)
        time = re.findall(r'发行时间：(.*?)</li>', html, re.I | re.S | re.M)
        if (len(songname) == 0):
            songname.append("")
        if (len(singer) == 0):
            singer.append("")
        if (len(liupai) == 0):
            liupai.append("")
        if (len(yuzhong) == 0):
            yuzhong.append("")
        if (len(time) == 0):
            time.append("")
        print(songname[0])
        print(singer[0].strip())
        print(liupai[0])
        print(yuzhong[0])
        print(time[0])
        item = [songname[0], singer[0], liupai[0], yuzhong[0],
                time[0][0:4]]
        print(item)
        with open('ku.txt', 'a', encoding='utf-8') as ku:
            ku.write(str(item) + '\n')


if __name__ == '__main__':
    line = 'https://y.qq.com/n/yqq/playlist/7349246858.html#stat=y_new.profile.create_playlist.click&dirid=23'
    getSongSheet(line)
