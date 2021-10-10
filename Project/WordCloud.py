import wordcloud
import jieba
import imageio
import os

mk = imageio.imread('D:\\Graduation_Project\\photo moduel\\wujiaoxing.png')
w = wordcloud.WordCloud(width = 1000,
                        height = 800,
                        background_color = 'white',
                        scale = 15,
                        mask = mk,
                        font_path = 'msyh.ttc',
                        stopwords={'多多捂脸', '多多耍酷', '多多大笑', '多多大哭', '多多比耶', '多多笑哭', '大哭', '大笑',
                                   '憨笑', '可爱', '狗', '便便', '狗', '哀伤', '爱心', '奸笑', '钻石', '龇牙', '礼物', '心碎',
                                    '流泪', '吐舌'}
                        )
file_dir = r"D:\Graduation_Project\Project\comments\OnlyComments"
a = os.walk(file_dir)
for root, dirs, files in os.walk(file_dir):
    print(files) #当前路径下所有非目录子文件
for each in files:
    with open('D:\\Graduation_Project\\Project\\comments\\OnlyComments\\{}'.format(each),'r',encoding ='utf-8') as f :
        print(f)
        txt = f.read()
        txtlist = jieba.lcut(txt)
        string = ''.join(txtlist)
        a = files[files.index(each)][:-4]
        w.generate(string)
        w.to_file('D:\\Graduation_Project\\Cloud photo\\wordcloud\\{}.jpg'.format(a))
