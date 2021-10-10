import re, os

"""将歌名和情感指数组合成列表"""
allmo = []
allus = []
relist0 = []
relist1 = []


with open(r'D:\Graduation_Project\Data\allemotion.txt', 'r', encoding='utf-8') as f:
    while True:
        # print('进入循环')
        textlist = f.readline()
        # print(textlist)
        if textlist == '':
            break
        else:
            textlist = textlist[:-1]
            pattern = r'[,]'
            result = re.split(pattern, textlist)
            allmo.append(result)
            # print(result)
            relist0.append(result[0])
            relist1.append(int(result[1][3:8]))
    # 排序前
    dic = dict(zip(relist0, relist1))
    # print(dic)
    # #排序后
    dict2 = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
    # print(dict2)
"""将歌名和文件大小组成列表"""

file_dir = r"D:\Graduation_Project\Project\comments\OnlyComments"

file_size = []
for root, dirs, files in os.walk(file_dir):
    pass

for each in files:
    temp = root + '\\' + each
    size = os.path.getsize(temp)
    file_size.append([each[:-4], size])

"""将歌名和情感系数和文件大小进行组合"""

for key, value in dict2.items():
    for each in file_size:
        if key == each[0]:
            dict2[key] = [value, each[1]]
# print(dict2)

"""中心化"""
size_value = []
mood_value = []
for key, value in dict2.items():
    mood_value.append(value[0])
    size_value.append(value[1])
max_mood = max(mood_value)
min_mood = min(mood_value)
max_size = max(size_value)
min_size = min(size_value)
for key, value in dict2.items():
    temp_mood = (value[0] - min_mood) / (max_mood - min_mood)
    temp_size = (value[1] - min_size) / (max_size - min_size)
    if temp_mood == 0:
        temp_mood = 0.0001
        dict2[key] = [temp_mood, float(str(temp_size)[:6])]
    elif temp_size == 0.0:
        temp_size = 0.0001
        dict2[key] = [float(str(temp_mood)[:6]), temp_size]
    else:
        dict2[key] = [float(str(temp_mood)[:6]), float(str(temp_size)[:6])]

# print(dict2)
# print(dict2["椿"])
# print(dict2["奇迹再现"])

"""歌名及标签"""

# dicre = {}
# def com_2():
with open(r'D:\Graduation_Project\Data\ku.txt', 'r', encoding='utf-8') as f1:
    while True:
        temp = f1.readline()[:-1]
        if temp == '':
            break
        else:
            Maindata = temp.replace("[", "").replace("]", ""). \
                replace('\\', '').replace(" '", ""). \
                replace("'", "").split(",")
            # print(Maindata)
            mainlist = [Maindata[0], [Maindata[1], Maindata[2], Maindata[3], Maindata[4]]]
            allus.append(mainlist)

for a in allus:
    for b in allmo:
        if a[0] == b[0]:
            a[1].append(b[1])
        else:
            pass

for each in allus:
    if len(each[1]) == 4:
        allus.remove(each)

with open(r'D:\Graduation_Project\Data\recommend.txt', 'w', encoding='utf-8') as f2:
    for each1 in allus:
        f2.write(str(each1) + '\n')

file_dir = r"D:\Graduation_Project\music"
i = 1
for root, dirs, files in os.walk(file_dir):
    i += 1
    break

reall = []
temp = []
for b in allus:
    for c in files:
        if b[0] + '.mp3' == c:
            reall.append(b)
            files.remove(c)

dicre = dict(reall)
with open(r'D:\Graduation_Project\Data\dicre.txt', 'w', encoding='utf-8') as f3:
    f3.write(str(dicre))
# print(dicre)
    # return dicre


# print(len(dicre))]

"""综合推荐"""


def com_3():
    com_re = dict(sorted(dicre.items(), key=lambda x: x[1][2], reverse=True))
    chinese = []
    english = []
    light = []
    other = []
    for key, value in com_re.items():
        if value[2] == "国语":
            chinese.append([key, value])
        elif value[2] == "英语":
            english.append([key, value])
        elif value[2] == "轻音乐":
            light.append([key, value])
        else:
            other.append([key, value])
    chinese.sort(key=lambda x: x[1][1])
    english.sort(key=lambda x: x[1][1])
    light.sort(key=lambda x: x[1][1])
    other.sort(key=lambda x: x[1][1])
    combin = chinese + english + light + other
    com_count = 0
    new_combin = {}
    for each in combin:
        new_combin[each[0]] = [int(each[1][3]), float(each[1][4]), com_count]
        com_count += 1
    # print(new_combin)
    # 标准化
    temp_year = []
    temp_motion = []
    temp_num = []
    for key, value in new_combin.items():
        temp_year.append(value[0])
        temp_motion.append(value[1])
        temp_num.append(value[2])
    max_tempyear = max(temp_year)
    min_tempyear = min(temp_year)
    max_tempmotion = max(temp_motion)
    min_tempmotion = min(temp_motion)
    max_tempnum = max(temp_num)
    min_tempnum = min(temp_num)
    for key, value in new_combin.items():
        value[0] = float(str((value[0] - min_tempyear) / (max_tempyear - min_tempyear))[:6])
        value[1] = float(str((value[1] - min_tempmotion) / (max_tempmotion - min_tempmotion))[:6])
        value[2] = float(str((value[2] - min_tempnum) / (max_tempnum - min_tempnum))[:6])
        if value[0] == 0:
            value[0] = 0.0001
        if value[1] == 0:
            value[1] = 0.0001
        if value[2] == 0:
            value[2] = 0.0001
    return new_combin



