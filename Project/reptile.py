# -*- coding:utf-8 -*-
#用于打开和读取URL
import urllib.request
import http.cookiejar
#用于解析URL
import urllib.parse
import json
import time
import codecs
from Crypto.Cipher import AES
import base64
import os
import requests
from bs4 import BeautifulSoup

class music:

    #初始化
    def __init__(self):
        #设置代理，以防止本地IP被封
        self.proxyUrl = "http://202.106.16.36:3128"
        #request headers,这些信息可以在ntesdoor日志request header中找到，copy过来就行
        self.Headers = {
            'Accept': "*/*",
            'Accept-Language': "zh-CN,zh;q=0.9",
            'Connection': "keep-alive",
            'Host': "music.163.com",
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"

        }

        # 使用http.cookiejar.CookieJar()创建CookieJar对象
        self.cjar = http.cookiejar.CookieJar()
        # 使用HTTPCookieProcessor创建cookie处理器，并以其为参数构建opener对象
        self.cookie = urllib.request.HTTPCookieProcessor(self.cjar)
        self.opener = urllib.request.build_opener(self.cookie)
        # 将opener安装为全局
        urllib.request.install_opener(self.opener)
        #第二个参数
        self.second_param = "010001"
        #第三个参数
        self.third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
        #第四个参数
        self.forth_param = "0CoJUm6Qyw8W8jud"



    def get_params(self, page):
        #获取encText，也就是params
        iv = "0102030405060708"
        first_key = self.forth_param
        second_key = 'F' * 16
        if page == 0:
            first_param = '{rid:"", offset:"0", total:"true", limit:"20", csrf_token:""}'
        else:
            offset = str((page - 1) * 20)
            first_param = '{rid:"", offset:"%s", total:"%s", limit:"20", csrf_token:""}' % (offset, 'false')
        self.encText = self.AES_encrypt(first_param, first_key, iv)
        self.encText = self.AES_encrypt(self.encText.decode('utf-8'), second_key, iv)
        return self.encText

    def AES_encrypt(self, text, key, iv):
        #AES加密
        pad = 16 - len(text) % 16
        text = text + pad * chr(pad)
        encryptor = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
        encrypt_text = encryptor.encrypt(text.encode('utf-8'))
        encrypt_text = base64.b64encode(encrypt_text)
        return encrypt_text

    def get_encSecKey(self):
        #获取encSecKey
        encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
        return encSecKey

    def get_json(self, url, params, encSecKey):
        # post所包含的参数
        self.post = {
            'params': params,
            'encSecKey': encSecKey,
        }
        # 对post编码转换
        self.postData = urllib.parse.urlencode(self.post).encode('utf8')
        try:
            #发出一个请求
            self.request = urllib.request.Request(url,self.postData,self.Headers)
        except urllib.error.HTTPError as e:
            print(e.code)
            print(e.read().decode("utf8"))
        #得到响应
        self.response = urllib.request.urlopen(self.request)
        #需要将响应中的内容用read读取出来获得网页代码，网页编码为utf-8
        self.content = self.response.read().decode("utf8")
        #返回获得的网页内容
        return self.content




    def get_hotcomments(self, list):
        #获取热门评论
        print ('第二个程序开始执行')
        global length
        global number
        length = (len(list))
        number = length
        params = self.get_params(1)
        encSecKey = self.get_encSecKey()
        for url in list:
            try:
                print('循环正在执行')
                content = self.get_json(url, params, encSecKey)
                json_dict = json.loads(content)
                hot_comment = json_dict['hotComments']
                musicname = list1[length-number]
                f = open('D:\Graduation_Project\Project\comments\HotComments\{}.txt'.format(musicname), 'a', encoding='utf-8')
                for i in hot_comment:
                    #将评论输出至txt文件中
                    time_local = time.localtime(int(i['time'] / 1000))  # 将毫秒级时间转换为日期
                    dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                    f.write('用户: ' + i['user']['nickname'] + '\n')
                    f.write('点赞数: ' + str(i['likedCount']) + '\n')
                    f.write('发表时间: ' + dt + '\n')
                    f.write('评论: ' + i['content'] + '\n')
                    f.write('-' * 40 + '\n')
                number  -= 1
                print('还有'+str(number)+'首歌曲就爬取完了')
            except:
                number -=1
                print('还有' + str(number) + '首歌曲就爬取完了')
                continue
        print('歌单全部热评提取完毕')
        f.close()



    def get_allcomments(self, list):
        #获取全部评论
        params = self.get_params(1)
        encSecKey = self.get_encSecKey()
        length = len(list)
        num = length
        list3 = []
        for url in list:
            try:
                content = self.get_json(url, params, encSecKey)
                json_dict = json.loads(content)
                comments_num = int(json_dict['total'])
                musicname = list1[length-num]
                present_page = 0
                if (comments_num % 20 == 0):
                    page = comments_num / 20
                else:
                    page = int(comments_num / 20) + 1
                print("共有%d页评论" % page)
                print("共有%d条评论" % comments_num)
                f = open(
                    'D:\Graduation_Project\Project\comments\AllComments\{}.{}.txt'.format(length - num + 1, musicname),
                    'w+', encoding='utf-8')
                # 逐页抓取
                for i in range(99):
                    params = self.get_params(i + 1)
                    encSecKey = self.get_encSecKey()
                    json_text = self.get_json(url, params, encSecKey)
                    json_dict = json.loads(json_text)
                    present_page = present_page + 1
                    for i in json_dict['comments']:
                        # 将评论输出至txt文件中
                        musicname = list1[length - num]
                        time_local = time.localtime(int(i['time'] / 1000))# 将毫秒级时间转换为日期
                        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
                        f.write('用户: ' + i['user']['nickname'] + '\n')
                        f.write('点赞数: ' + str(i['likedCount']) + '\n')
                        f.write('发表时间: ' + dt + '\n')
                        f.write('评论: ' + i['content'] + '\n')
                        f.write('-' * 40 + '\n')
                        list3.append(i['content'])
                    print('第%d页已经爬取完毕，还剩%d页就完成了'%(present_page,(100-present_page)))
                f.close()
                f = open('D:\Graduation_Project\Project\comments\OnlyComments\{}.{}.txt'.format(length-num+1,musicname), 'w+', encoding='utf-8')
                f.write(''.join(list3) + '\n')
                f.close()
                list3.clear()
                num -= 1
                print('还有' + str(num) + '首歌曲就爬取完了')
            except:
                num -= 1
                print('还有' + str(num) + '首歌曲就爬取完了')
                continue
            #print("第%d页抓取完毕" % present_page)


    def musiclist (self):
        play_url = 'http://music.163.com/playlist?id=2305812129'
        s = requests.session()
        response = s.get(play_url, headers=self.Headers).content
        # 使用bs4匹配出对应的歌曲名称和地址
        s = BeautifulSoup(response, 'lxml')
        main = s.find('ul', {'class': 'f-hide'})
        # print(main.find_all('a'))
        global list,list1
        list = []
        list1 = []
        # file = open('musiclist.txt', 'w', encoding='utf-8')
        for music in main.find_all('a'):
            # print('{} : {}'.format(music.text, music['href']))
            musicUrl = 'http://music.163.com/song/media/outer/url' + music['href'][5:] + '.mp3'
            musicName = music.text
            # print(musicName)
            list1.append(musicName)
            musicid = music['href'][9:]
            url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token".format(musicid)
            list.append(url)
        print('第一个程序执行完毕')
        print(list)
        print(list1)

            # 单首歌曲的名字和地址放在list列表中
            # list.append(musicName)
            # list.append(musicUrl)
            # 全部歌曲信息放在lists列表中
            # lists.append(list)
            # file.write(str(list))




mail = music()
mail.musiclist()
# mail.get_hotcomments(list)
mail.get_allcomments(list)

