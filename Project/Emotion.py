import snownlp
import jieba
import os
import re
#情感分析

list = []
file_dir = r"D:\Graduation_Project\Project\comments\OnlyComments"
a = os.walk(file_dir)
for root, dirs, files in a:
    print(files)
for each in files:
    print(each)
    with open(r"D:\Graduation_Project\Project\comments\OnlyComments\{}".format(each),encoding='utf-8') as f:
        fa= f.read()
        txtlist = jieba.lcut(fa)
    with open(r'D:\Graduation_Project\Cloud photo\Emontion\{}'.format(each),'w',encoding= 'utf-8') as fb:
        for each1 in txtlist:
            mood = snownlp.SnowNLP(each1)
            feeling = mood.sentiments
            # list.append(feeling)
            fb.write(str(feeling)+'\n')
            # print(feeling)
#算平均数
    with open(r'D:\Graduation_Project\Cloud photo\Emontion\{}'.format(each), 'r', encoding='utf-8') as fb:

        Anum = 0
        count = 0
        while True:
            fc = fb.readline()
            if fc == '':
                break
            else:
                fc =fc[:-1]
                # print(fc)
                each2 = float(fc)
                Anum = each2+Anum
                count +=1
                # print(Anum, count)

        ans = Anum / count
        ans = str(ans)[0:10]
    with open(r'D:\Graduation_Project\Cloud photo\allemotion.txt','a',encoding= 'utf-8') as fd:

        result = re.findall(r'[.](.*)[.]', each)
        result = ''.join(result)
        result.replace(u'\xa0', u' ')
        fd.write(result+','+ans+'\n')
        print(ans)






