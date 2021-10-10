import tkinter
from tkinter import messagebox
from tkinter.ttk import Progressbar
from mutagen.mp3 import MP3
import pygame
import random
import shutil
import time
from tkinter.filedialog import *
from tkinter import *
from PIL import Image, ImageTk
import re
from pymediainfo import MediaInfo
from threading import Thread
import Data
from Project import Downmusic, sys_volume

# 导入环境
folder_path = r"D:\Graduation_Project\Music"
folder_list = os.listdir(folder_path)  # 遍历文件夹里面每个文件
listall = []
listall_Backup = []
count = 0
for i in folder_list:  # 将文件夹里的文件按顺序传提给变量i  此处区别os.walk()
    if os.path.splitext(i)[1] == '.mp3':  # 提取特定后缀文件'.***'
        fil = folder_path + "\\" + i
        listall.append(fil)
        listall_Backup.append(fil)
        count += 1
relist = []
re_fina = []


def playmusic():  # 开始播放
    global Musicname, Musicname1
    pygame.mixer.music.load(listall[0])
    pygame.mixer.music.play()
    Musicname = listall[0][28:-4]
    print(Musicname)
    Musicname1 = "        " + listall[0][28:-4]
    print(Musicname1)
    dagou()
    pbrun()


# 下一首
index = 0
reindex = 0
re_index = 0
re_ou_index = 0
love_index = -1.1


def loops():
    global index, reindex, love_index, Musicname, Musicname1, con
    con = 1
    if not var2.get() and not var3.get() and not var4.get():
        # 喜爱音乐播放
        if create_num == 1 and var.get() == 4 and love_index != -1.1:
            if love_index < len(listlove) - 1:
                love_index += 1
            else:
                love_index = 0
            love_fil = folder_path + "\\" + listlove[love_index] + '.mp3'
            pygame.mixer_music.load(love_fil)
            pygame.mixer_music.play()
            Musicname = listlove[love_index]
            Musicname1 = "        " + listlove[love_index]
        # 正常音乐播放
        else:
            if index < len(listall) - 1:
                index += 1
            else:
                index = 0
            pygame.mixer.music.load(listall[index])
            pygame.mixer.music.play()
            Musicname = listall[index][28:-4]
            Musicname1 = "        " + listall[index][28:-4]
        c1.set(0)
        dagou()
        pbrun()
    elif var3.get():
        if reindex < len(relist) - 1:
            reindex += 1
        else:
            reindex = 0
        loops_fil = folder_path + "\\" + relist[reindex] + '.mp3'
        pygame.mixer.music.load(loops_fil)
        pygame.mixer.music.play()
        Musicname = relist[reindex]
        Musicname1 = '        ' + relist[reindex]
        c1.set(0)
        dagou()
        pbrun()
    elif var4.get():
        global re_ou_index
        if re_ou_index < len(re_ou_shi) - 1:
            re_ou_index += 1
        else:
            re_ou_index = 0
        loops_fil = folder_path + "\\" + re_ou_shi[re_ou_index] + '.mp3'
        pygame.mixer.music.load(loops_fil)
        pygame.mixer.music.play()
        Musicname = re_ou_shi[re_ou_index]
        Musicname1 = '        ' + re_ou_shi[re_ou_index]
        c1.set(0)
        dagou()
        pbrun()
    else:
        global re_index
        if re_index < len(re_fina) - 1:
            re_index += 1
        else:
            re_index = 0
        re_fina_file = folder_path + "\\" + re_fina[re_index] + '.mp3'
        pygame.mixer.music.load(re_fina_file)
        pygame.mixer.music.play()
        Musicname = re_fina[re_index]
        Musicname1 = "        " + re_fina[re_index]
        c1.set(0)
        dagou()
        pbrun()


def previous():
    global index, reindex, love_index, Musicname, Musicname1, con
    con = 1
    if not var2.get() and not var3.get() and not var4.get():
        if create_num == 1 and var.get() == 4 and love_index != -1.1:
            if love_index < len(listlove) - 1:
                love_index -= 1
            else:
                love_index = 0
            love_fil = folder_path + "\\" + listlove[love_index] + '.mp3'
            pygame.mixer_music.load(love_fil)
            pygame.mixer_music.play()
            Musicname = listlove[love_index]
            Musicname1 = "        " + listlove[love_index]
        else:
            if index <= 0:
                return
            else:
                if index < len(listall) - 1:
                    index -= 1
                else:
                    index = 0
                pygame.mixer.music.load(listall[index])
                pygame.mixer.music.play()
                Musicname = listall[index][28:-4]
                Musicname1 = "        " + listall[index][28:-4]
        c1.set(0)
        dagou()
        pbrun()
    elif var3.get():
        if reindex <= 0:
            return
        else:
            if reindex < len(relist) - 1:
                reindex -= 1
            else:
                reindex = 0
            pre_fil = folder_path + "\\" + relist[reindex] + '.mp3'
            pygame.mixer.music.load(pre_fil)
            pygame.mixer.music.play()
            Musicname = relist[reindex]
            Musicname1 = '        ' + relist[reindex]
            c1.set(0)
            dagou()
            pbrun()
    elif var4.get():
        global re_ou_index
        if re_ou_index <= 0:
            return
        else:
            if re_ou_index < len(re_ou_shi) - 1:
                re_ou_index -= 1
            else:
                re_ou_index = 0
            loops_fil = folder_path + "\\" + re_ou_shi[re_ou_index] + '.mp3'
            pygame.mixer.music.load(loops_fil)
            pygame.mixer.music.play()
            Musicname = re_ou_shi[re_ou_index]
            Musicname1 = '        ' + re_ou_shi[re_ou_index]
            c1.set(0)
            dagou()
            pbrun()
    else:
        global re_index
        if re_index <= 0:
            return
        else:
            if re_index < len(re_fina) - 1:
                re_index -= 1
            else:
                re_index = 0
            re_fina_file = folder_path + "\\" + re_fina[re_index] + '.mp3'
            pygame.mixer.music.load(re_fina_file)
            pygame.mixer.music.play()
            Musicname = re_fina[re_index]
            Musicname1 = "        " + re_fina[re_index]
            c1.set(0)
            dagou()
            pbrun()


# 随机播放
def selectpath():  # 随机播放
    if demoStatus.get() or demoStatus1.get():
        demoStatus.set(False)
        demoStatus1.set(False)
    if demoStatus2.get():
        s = random.randint(0, (count - 1))  # 获取随机数
        file = listall[s]
        pygame.mixer.music.load(file)
        global Musicname, Musicname1, con
        con = 1
        pygame.mixer.music.play(1, 0)
        random.shuffle(listall)
        Musicname = file[28:-4]
        Musicname1 = '        ' + file[28:-4]
        c1.set(0)
        dagou()
        pbrun()


# 单曲循环
def single_music():
    if demoStatus.get() or demoStatus2.get():
        demoStatus.set(False)
        demoStatus2.set(False)


# 顺序播放
def normal():
    if not demoStatus1.get() and not demoStatus2.get():
        demoStatus.set(True)
        return
    if demoStatus1.get() or demoStatus2.get():
        demoStatus1.set(False)
        demoStatus2.set(False)
    if demoStatus.get():
        global listall, listall_Backup, Musicname, Musicname1, con
        con = 1
        listall = listall_Backup.copy()
        pygame.mixer.music.load(listall[index])
        pygame.mixer.music.play()
        Musicname = listall[index][28:-4]
        Musicname1 = "        " + listall[index][28:-4]
        c1.set(0)
        dagou()
        pbrun()


def dagou():
    if listlove.count(Musicname) == 0:
        cblove.deselect()
    else:
        cblove.select()


def gai_volume():
    global gai_yin
    if gai_yin == 1:
        gai_yin = 0
    else:
        gai_yin = 1


gai_yin = 1


# 进度音量
def print_scale(text):
    if gai_yin == 0:
        velum = int(text)
        sys_volume.test(velum / 100)
    else:
        velum = int(text)
        pygame.mixer.music.set_volume(velum / 100)


def jd_scale(self):
    global path, Musicname, con
    if Musicname == '':
        c1.set(0)
    else:
        con = 1
        jd_fil = folder_path + "\\" + Musicname + '.mp3'
        audio = MP3(jd_fil)
        m = audio.info.length
        t1 = c1.get()
        c1.config(to=m)
        pygame.mixer.init()
        # if c1.get() == 0:
        #     return
        # else:
        pygame.mixer.music.load(jd_fil)
        pygame.mixer.music.play(1, t1)


# 自动切换，进度条
def pbrun():
    global Musicname
    pb_fil = folder_path + "\\" + Musicname + '.mp3'
    # print(Musicname)
    media_info = MediaInfo.parse(pb_fil)
    # print(fil)
    data = media_info.to_json()  # media到json()这两行是获取文件的所有属性
    rst = re.search('other_duration.*?(.*?)min(.*?)s.*?', data)
    music_min = int(rst.group(0)[19:20])
    r = int(rst.group(0)[-4:-2])
    all_time = music_min * 60 + r
    # print(all)
    pb['maximum'] = all_time
    now = 0

    while now < all_time:
        if quittop == 0:
            if not pygame.mixer_music.get_busy():
                pb['value'] = 0
                return
            else:
                now = pygame.mixer.music.get_pos()
                now = now // 1000 + c1.get()
                # print(now)
                pb['value'] = now
                top.update()
                time.sleep(0.1)
        else:
            return
    if demoStatus1.get():
        c1.set(0)
        pbrun()
    else:
        loops()


# 右键菜单
def show_popupmenu(event):
    popupmenu.post(event.x_root, event.y_root)


def callback():  # 搜索本地文件
    path_ = askopenfilenames(filetypes=[("mp3 file", "*.mp3"), ("all", "*.*")])
    return path_


def play():  # 播放音乐
    try:
        f = callback()  # 选择制定文件
        f = f[0]
        pygame.mixer.music.load(f)
        pygame.mixer.music.play()
        global path, con
        con = 1
        path = f
        pathn.set(f)
    except IndexError:
        print('没有选择文件')


def stop():
    global Musicname1, Musicname
    a = pygame.mixer.music.get_busy()
    if a:
        Musicname1 = ' '
        Musicname = ''
        c1.set(0)
        w1.set(0)
        pygame.mixer.music.stop()  # 停止播放
    else:
        playmusic()


con = 1


def pa_un(event):
    global con
    if con == 1:
        pygame.mixer_music.pause()
        con = 0
    else:
        pygame.mixer_music.unpause()
        con = 1


def bu_pa_un():
    global con
    print(con)
    if con == 1:
        pygame.mixer_music.pause()
        con = 0
        print(con)
    else:
        pygame.mixer_music.unpause()
        con = 1
        print(con)


def choosepic():  # 保存的路径不能有中文，若需要中文则吧/换成\
    try:
        path_s = askopenfilename()
        img = ImageTk.PhotoImage(Image.open(path_s))
        l1.config(image=img)
        l1.image = img
    except AttributeError:
        print('没有选择图片')


# 切换音乐列表输入框
def choosemusiclist():
    num = var.get()
    print(num)
    if num == 3:
        o1.delete(0, END)
        find()
    elif num == 4:
        o1.delete(0, END)
        find_love()
    else:
        o1.delete(0, END)
        findre()


def find():
    find_path = r"D:\Graduation_Project\Music"
    find_list = os.listdir(find_path)  # 遍历文件夹里面每个文件
    list_find = []
    for each in find_list:  # 将文件夹里的文件按顺序传提给变量i  此处区别os.walk()
        if os.path.splitext(each)[1] == '.mp3':  # 提取特定后缀文件'.***'
            each = each[0:-4]
            list_find.append(each)
            o1.insert("end", each)


def find_love():
    if listlove is None:
        pass
    else:
        for each in listlove:
            o1.insert("end", each)


def findre():
    if re_fina is None or relist is None or re_ou_shi is None:
        pass
    else:
        if var3.get():
            if reindex >= 20:
                for each in relist:
                    if relist.index(each) == 40:
                        break
                    else:
                        o1.insert("end", each)
            else:
                for each in relist:
                    if relist.index(each) == 20:
                        break
                    else:
                        o1.insert("end", each)
        elif var4.get():
            print("a")
            if re_ou_index >= 20:
                for each in re_ou_shi:
                    if re_ou_shi.index(each) == 40:
                        break
                    else:
                        o1.insert("end", each)
            else:
                for each in re_ou_shi:
                    if re_ou_shi.index(each) == 20:
                        break
                    else:
                        o1.insert("end", each)
        elif var2.get():
            if re_index >= 20:
                for each in re_fina:
                    if re_fina.index(each) == 40:
                        break
                    else:
                        o1.insert("end", each)
            else:
                for each in re_fina:
                    if re_fina.index(each) == 20:
                        break
                    else:
                        o1.insert('end', each)


def music_book():
    save_button.config(state='normal')
    t.delete('1.0', 'end')
    with open(r'D:\Graduation_Project\Data\music_note.txt', 'r', encoding='utf-8') as f:
        txt = f.read()
        t.insert(END, txt)
    now_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    t.insert(END, "\n音乐：" + Musicname + "\n时间：" + now_time + "\n心情：" + "\n内容：")


def save():
    with open(r'D:\Graduation_Project\Data\music_note.txt', 'w+', encoding='utf-8') as f:
        txt = t.get("1.0", "end")
        f.write(txt)
    messagebox.showinfo("提示", "已保存到音乐日记！")


def find_hot():
    save_button.config(state='disabled')
    if pygame.mixer_music.get_busy():
        try:
            t.delete('1.0', 'end')
            with open('D:\\Graduation_Project\\Project\\comments\\HotComments\\{}.txt'.format(Musicname), 'r',
                      encoding='utf-8') as f:
                txt = f.read()
                # print('读取完毕',txt)
                t.insert(END, txt)
        except FileNotFoundError:
            t.insert(END, '很抱歉，该首曲子的评论飞走了~~')
    else:
        t.delete('1.0', 'end')
        txt = '你还没有开始放音乐，看什么评论!!!'
        t.insert(END, txt)


def music_add():
    try:
        music_dir = r'D:\Graduation_Project\Music'
        if not os.path.exists(music_dir):
            os.mkdir(music_dir)
        fi = callback()
        fi = fi[0]
        shutil.copy(fi, music_dir)
        name = str(os.path.basename(fi))
        o1.insert("0", name[:-4])
        add_fil = folder_path + '\\' + name
        print(add_fil)
        listall.append(add_fil)
    except IndexError:
        print('你没有选择文件啊')


# 点击播放
def get_mu(self):
    get_mu_dir = r'D:\Graduation_Project\Music'
    music_name = o1.get(o1.curselection())
    print(music_name)
    file = os.path.join(get_mu_dir, music_name + '.mp3')
    print(file)
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    global Musicname1, Musicname, index, re_index, love_index, reindex, re_ou_index, con
    con = 1
    Musicname = file[28:-4]
    Musicname1 = '        ' + file[28:-4]
    num = var.get()
    if num == 3:
        index = listall.index(file)
    elif num == 4:
        love_index = listlove.index(Musicname)
    elif var3.get() and num == 5:
        reindex = relist.index(Musicname)
    elif var4.get() and num == 5:
        re_ou_index = re_ou_shi.index(Musicname)
    else:
        re_index = re_fina.index(Musicname)
    c1.set(0)
    dagou()
    pbrun()


def word_cloud():
    root1 = tkinter.Toplevel()
    global Musicname
    mame = tkinter.Label(root1, text=Musicname, height=3, font=('隶书', 20))
    mame.pack()
    try:
        photo = Image.open(r"D:\Graduation_Project\Cloud photo\wordcloud\{}.jpg".format(Musicname))  # file：t图片路径
        photo = photo.resize((700, 600))
        global p
        p = ImageTk.PhotoImage(photo)
        wo_lb = Label(root1, image=p)  # 把图片整合到标签类中
        wo_lb.pack()  # 自动对齐
    except FileNotFoundError:
        mame.config(text='这张词云跑丢了')


def download():
    def in_down():
        name = entry.get()
        if len(name) == 0:
            dola.config(text='输入框不能为空哦！')
            time.sleep(3)
            dola.config(text='请输入下载的音乐： ')
        else:
            downb.config(state=DISABLED)
            entry.config(state=DISABLED)
            dola.config(text='正在下载，请稍后！')
            Downmusic.get_music_name(name)
            dola.config(text='下载完毕，请试听！')
            downb.config(state=NORMAL)
            entry.config(state=NORMAL)
            entry.delete(0, END)
            new_music = folder_path + "\\" + Downmusic.song_name + '.mp3'
            pygame.mixer_music.load(new_music)
            pygame.mixer_music.play()
            global Musicname1, Musicname, con
            con = 1
            Musicname = Downmusic.song_name
            Musicname1 = '         ' + Downmusic.song_name
            time.sleep(3)
            dola.config(text='请输入下载的音乐： ')

    threads = Thread(target=in_down)
    threads.start()


# 副窗口
def create():
    quku.config(state=DISABLED)
    global create_num
    create_num = 1
    top1 = tkinter.Toplevel()
    top1.title('Song library')
    top1.geometry("800x600+490+100")
    top1.configure(bg='LightBlue')
    top1.resizable(0, 0)
    top1.iconbitmap(r'D:\Graduation_Project\bankground\yinfu.ico')
    # 滚动条
    scrollbar = Scrollbar(top1)
    scrollbar.pack(side=RIGHT, fill=Y)
    scrollbar1 = Scrollbar(top1)
    scrollbar1.pack(side=RIGHT, fill=Y)

    topca = tkinter.Canvas(top1,
                           width=950,  # 指定Canvas组件的宽度
                           height=600,  # 指定Canvas组件的高度
                           bg='LightBlue')  # 指定Canvas组件的背景色
    imagen = Image.open(r"D:\Graduation_Project\bankground\主窗口背景12.jpg")
    imagen = imagen.resize((900, 600 + 50))
    global imn
    imn = ImageTk.PhotoImage(imagen)
    topca.create_image(300 + 50, 275, image=imn)  # 使用create_image将图片添加到Canvas组件中
    topca.pack()  # 将Canvas添加到主窗口
    global o1, t
    o1 = Listbox(top1, width=32, height=20, yscrollcommand=scrollbar1.set, selectmode="brose", font='幼圆')
    scrollbar1.config(command=o1.yview)
    o1.place(x=60, y=120)
    find()
    o1.bind("<Double-Button-1>", get_mu)

    # 设置两个按钮
    global var
    var = IntVar()
    var.set(3)
    rball = Radiobutton(top1, text='全部', variable=var, value=3, command=choosemusiclist, fg="Blue3", font='幼圆')
    rball.place(x=60, y=80)
    rblove = Radiobutton(top1, text='热爱', variable=var, value=4, command=choosemusiclist, fg="Blue3", font='幼圆')
    rblove.place(x=180, y=80)
    rbre = Radiobutton(top1, text='推荐', variable=var, value=5, command=choosemusiclist, fg="Blue3", font='幼圆')
    rbre.place(x=120, y=80)
    Button(top1, text='清空喜爱', relief="ridge", command=clearlove, width=10,  fg="Blue3", font='幼圆').place(x=240, y=80)
    # print(var.get())

    Button(top1, text='本地添加', command=music_add, width=12, fg="Blue3", font='幼圆').place(x=60, y=480)
    Button(top1, text='音乐日记', relief="ridge", command=music_book, width=12, fg="Blue3", font='幼圆').place(x=390, y=480)
    global save_button
    save_button = Button(top1, text='保存', relief="ridge", command=save, width=12, state='disabled', fg="Blue3", font='幼圆')
    save_button.place(x=490, y=480)
    m1 = Label(top1, text='播放歌单', width=15, font=("幼圆", 20), fg="Blue3")
    m1.place(x=80, y=20)

    # 热门评论框
    t = Text(top1, height=21, width=40, yscrollcommand=scrollbar.set, font='幼圆')
    scrollbar.config(command=t.yview)
    t.place(x=390, y=120)
    t.insert(END, '\n               赠 花 卿 \n\n'
                  '                唐·杜甫\n\n'
                  '         锦 城 丝 管 日 纷 纷，\n\n'
                  '         半 入 江 风 半 入 云 。\n\n'
                  '         此 曲 只 应 天 上 有，\n\n'
                  '         人 间 能 得 几 回 闻 。\n\n\n\n\n\n\n'
                  'Tips: 开启音乐后，点击上方切换评论按钮，\n\n即可收看精彩评论')
    Button(top1, text='切换评论', command=find_hot, width=10, fg="Blue3", font='幼圆').place(x=390, y=80)

    Button(top1, text='显示词云', command=word_cloud, width=10, fg="Blue3", font='幼圆').place(x=490, y=80)
    o1.bind("<Double-Button-1>", get_mu)
    m2 = Label(top1, text='热门评论', width=15, font=("幼圆", 20),fg="Blue3")
    m2.place(x=440, y=20)

    global entry, dola, downb
    dola = Label(top1, text='请输入下载的音乐： ', font=('幼圆', 20), height=1, fg="Blue3")
    dola.place(x=60, y=530)
    entry = Entry(top1, font=('隶书', 23), width=15)
    entry.place(x=310, y=530)

    downb = Button(top1, text='开始下载', font=('幼圆', 15), command=download, fg="Blue3")
    downb.place(x=570, y=530)

    def closes():
        quku.config(state=NORMAL)
        top1.destroy()

    top1.protocol("WM_DELETE_WINDOW", closes)


# 推荐系统
def recommend():
    if var3.get() or var4.get():
        var3.set(False)
        var4.set(False)
    if var2.get():
        if len(listlove) == 0:
            l2.config(text='请添加喜爱歌曲后再开始推荐系统')
            cbre.deselect()
        else:
            global Musicname, Musicname1, con
            con = 1
            if len(listlove) == 1:
                add_re()
            else:
                global re_fina
                loveall = []  # 喜爱音乐
                lovedeep = []  # 重复的关键词
                temp_list = []  # 排序前的关键词和数量
                # 求喜爱音乐的全部信息（不含歌名）
                for eal in listlove:
                    for key, value in Data.dicre.items():
                        if eal == key:
                            for each in value:
                                if each == value[4]:
                                    loveall.append(each[:4])
                                else:
                                    loveall.append(each)
                print(loveall)
                # 计算关键字出现的次数
                for each in loveall:
                    num = loveall.count(each)
                    temp_list.append([each, num])
                for each in temp_list:
                    if each not in lovedeep:
                        lovedeep.append(each)
                lovedeep.sort(key=lambda x: x[1], reverse=True)
                print(lovedeep)
                new_lovedeep = lovedeep[:]  # 防止for循环和remove的冲突
                for each in lovedeep:
                    if (each[1] == 1) or (each[0] == ''):
                        new_lovedeep.remove(each)
                lovedeep = new_lovedeep
                print(lovedeep)
                # 根据最多关键字匹配歌曲
                re_list = []  # 符合条件的歌曲
                re_temp = []  # 每种歌曲和其对应的数量
                re_fina = []  # 最终的推荐歌单
                for each in lovedeep:
                    for key, value in Data.dicre.items():
                        for eava in value:
                            if (each[0] == eava) or (each[0] == eava[:4]):
                                key_count = 0
                                while key_count < each[1]:
                                    re_list.append(key)
                                    key_count += 1
                print(re_list)
                for each in re_list:
                    musicnum = re_list.count(each)
                    re_temp.append([each, musicnum])
                print(re_temp)
                for each in re_temp:
                    if each not in re_fina:
                        re_fina.append(each)
                re_fina.sort(key=lambda x: x[1], reverse=True)
                print(re_fina)
                re_fina_temp = re_fina[:]
                for each in listlove:
                    for eafi in re_fina:
                        if each == eafi[0]:
                            re_fina_temp.remove(eafi)
                re_fina = re_fina_temp
                print(re_fina)
                del re_fina_temp
                re_fina_temp = []
                for each in re_fina:
                    re_fina_temp.append(each[0])
                re_fina = re_fina_temp
                print(re_fina)
                if len(re_fina) == 0:
                    add_re()
                else:
                    re_fil = folder_path + "\\" + re_fina[0] + '.mp3'
                    print(re_fil)
                    pygame.mixer_music.load(re_fil)
                    pygame.mixer_music.play()
                    Musicname = re_fina[re_index]
                    Musicname1 = "        " + re_fina[re_index]
                    dagou()
                    pbrun()


cos_list = []


def add_re():
    if var2.get() or var4.get():
        var2.set(False)
        var4.set(False)
    if var3.get():
        temp_mood = []
        temp_size = []
        for each in listlove:
            for key, value in Data.dict2.items():
                if each == key:
                    temp_mood.append(value[0])
                    temp_size.append(value[1])
        avg_mood = sum(temp_mood) / len(temp_mood)
        avg_size = sum(temp_size) / len(temp_size)
        print(avg_mood, avg_size)
        for key, value in Data.dict2.items():
            minus_x = value[0] - avg_mood
            minus_y = value[1] - avg_size
            new_avg_mood = avg_mood - minus_x
            new_avg_size = avg_size - minus_y
            new_value_x = value[0] - minus_x
            new_value_y = value[1] - minus_y
            cos = (new_avg_mood * new_value_x + new_avg_size * new_value_y) / \
                  ((((new_avg_mood ** 2) + (new_avg_size ** 2)) ** (1 / 2)) * (
                          ((new_value_x ** 2) + (new_value_y ** 2)) ** (1 / 2)))
            cos_list.append([key, cos])
        cos_list.sort(key=lambda x: x[1], reverse=True)
        print(cos_list)
        temp_list = []
        for each in cos_list:
            temp_list.append(each[0])
        files = ''
        for root, dirs, files in os.walk(folder_path):
            pass
        for each in temp_list:
            for every in files:
                if each == every[:-4]:
                    relist.append(each)
        pygame.mixer_music.load(folder_path + '\\' + relist[0] + '.mp3')
        pygame.mixer_music.play()
        global Musicname, Musicname1, con
        con = 1
        Musicname = relist[0]
        Musicname1 = '         ' + relist[0]
        dagou()
        pbrun()


re_ou_shi = []


def comprehensive():
    if var3.get() or var2.get():
        var3.set(False)
        var2.set(False)
    if var4.get():
        catch_year = []
        catch_mood = []
        catch_num = []
        new_combin = Data.com_3()
        for each in listlove:
            for key, value in new_combin.items():
                if each == key:
                    catch_year.append(value[0])
                    catch_mood.append(value[1])
                    catch_num.append(value[2])
        avg_love = [sum(catch_year) / len(catch_year),
                    sum(catch_mood) / len(catch_mood),
                    sum(catch_num) / len(catch_num)]
        print(avg_love)
        print(new_combin["刚刚好"])
        print(new_combin["Lemon"])
        ou_shi = []
        for key, value in new_combin.items():
            ou_shi.append([key, (((avg_love[0] - value[0]) ** 2) * 0.5 +
                                 (avg_love[1] - value[1]) ** 2 + (avg_love[2] - value[2]) ** 2) ** (1 / 2)])
        ou_shi.sort(key=lambda x: x[1])
        print(ou_shi)
        for each in ou_shi:
            re_ou_shi.append(each[0])
        pygame.mixer_music.load(folder_path + '\\' + re_ou_shi[0] + '.mp3')
        pygame.mixer_music.play()
        global Musicname, Musicname1, con
        con = 1
        Musicname = re_ou_shi[0]
        Musicname1 = '         ' + re_ou_shi[0]
        dagou()
        pbrun()


# 喜爱列表
listlove = []
with open(r'D:\Graduation_Project\Data\lovemusic.txt', 'r', encoding='utf-8') as love:
    while True:
        single = love.readline()[:-1]
        if single == '':
            break
        else:
            listlove.append(single)


def lovemusic():
    global Musicname
    temp = pygame.mixer.music.get_busy()
    if not temp:
        l2.config(text='还没有选择歌曲')
        cblove.deselect()
    else:
        if var1.get():
            listlove.append(Musicname)
            print(listlove)
            with open(r'D:\Graduation_Project\Data\lovemusic.txt', 'a', encoding='utf-8') as love_1:
                love_1.write(Musicname + '\n')

        else:
            listlove.remove(Musicname)
            with open(r'D:\Graduation_Project\Data\lovemusic.txt', 'r', encoding='utf-8') as fb:
                lines = fb.readlines()
                with open(r'D:\Graduation_Project\Data\lovemusic.txt', 'w', encoding='utf-8') as f:
                    for line in lines:
                        if line.strip("\n") != Musicname:
                            f.write(line)


def clearlove():
    ret = messagebox.askyesno("Clear love", "真的要清空吗？")
    if ret:
        with open(r'D:\Graduation_Project\Data\lovemusic.txt', 'w', encoding='utf-8'):
            global listlove
            listlove = []
    else:
        return


# 多线程实现滚动音乐名
quittop = 0

def gundong():
    global Musicname1, threads1
    while True:
        if quittop == 0:
            # print(Musicname1)
            Musicname1 = Musicname1[1:] + Musicname1[0]

            l2.config(text=Musicname1)
            time.sleep(0.5)
        else:
            break


def close():
    global quittop
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        quittop = 1
        top.destroy()



top = tkinter.Tk()

top.title('Music Player')
top.geometry('300x600+200+100')
top.iconbitmap(r'D:\Graduation_Project\bankground\yinfu.ico')
top.resizable(0, 0)
canvas = tkinter.Canvas(top,
                        width=300,  # 指定Canvas组件的宽度
                        height=600,  # 指定Canvas组件的高度
                        bg='LightBlue')  # 指定Canvas组件的背景色
image = Image.open("D:\\Graduation_Project\\bankground\\主窗口背景10.jpg")
im = ImageTk.PhotoImage(image)
#
canvas.create_image(342 - 100, 200 + 100, image=im)
canvas.pack()  # 将Canvas添加到主窗口

# canvas.create_arc(10, 140, 130, 250, extent=359,style=ARC, width=3)
# canvas.create_arc(180, 140, 300, 250, extent=359,style=ARC,width=3)


pygame.init()
path = r'D:\Graduation_Project\Music'
pathn = StringVar()

v = StringVar()
v1 = StringVar()
if __name__ == '__main__':
    l1 = Label(top)  # 图片放置位置
    l1.place(x=-10, y=0)

    Musicname = ''
    create_num = 0

    # 随机播放
    # Button(top, text="随机播放", command=selectpath, width=7, bg="#747eb9", font='华文行楷').place(x=215, y=360)
    load = Image.open("D:\\Graduation_Project\\bankground\\播放.jpg")
    render = ImageTk.PhotoImage(load)
    load1 = Image.open("D:\\Graduation_Project\\bankground\\下一首.jpg")
    render1 = ImageTk.PhotoImage(load1)
    load2 = Image.open("D:\\Graduation_Project\\bankground\\上一首.jpg")
    render2 = ImageTk.PhotoImage(load2)
    Button(top, image=render1, command=loops, width=20, height=20).place(x=180, y=300)
    Button(top, image=render2, command=previous, width=20, height=20).place(x=100, y=300)
    # 音乐名
    l2 = Label(top, text='', width=12, font=("幼圆", 30),fg="Blue3")
    l2.place(x=30, y=70)

    # 音乐名滚动
    Musicname1 = '                      欢迎来到音乐播放系统'
    threads1 = Thread(target=gundong)
    threads1.start()

    # 暂停，开始播放，结束播放
    Button(top, image=render, command=bu_pa_un, width=20, height=20, font='幼圆').place(x=140, y=300)
    Button(top, text="开始/结束", command=stop, width=8,  font='幼圆', fg='Blue3').place(x=23, y=20)

    # 曲库
    quku = Button(top, text="♬曲库", command=create, width=8,  font='幼圆', fg="Blue3")
    quku.place(x=220, y=20)

    # Button(top, text="测试按钮", command= stop, width=7, bg="sky blue").place(x=100, y=300)

    # 开启个性化推荐
    var2 = BooleanVar()
    var2.set(False)
    cbre = Checkbutton(top, text='标签\n推荐', variable=var2, command=recommend, font='幼圆', fg="Blue3")
    cbre.place(x=23, y=370)

    var3 = BooleanVar()
    var3.set(False)
    cbre_one = Checkbutton(top, text='情感\n推荐', variable=var3, command=add_re, font='幼圆', fg="Blue3")
    cbre_one.place(x=119, y=370)

    var4 = BooleanVar()
    var4.set(False)
    cb_com = Checkbutton(top, text='综合\n推荐', variable=var4, command=comprehensive,font='幼圆', fg="Blue3")
    cb_com.place(x=215, y=370)

    var1 = BooleanVar()
    var1.set(False)
    cblove = Checkbutton(top, text='❤喜爱', cursor="heart", variable=var1, command=lovemusic, offvalue=0, font='幼圆',
                         fg="Blue3")
    cblove.place(x=200, y=170)

    # 音量
    w1 = Scale(top, from_=0, to=100, orient="horizontal", length=254, variable=v, command=print_scale, label="音量",
               width=13, showvalue='0', font='幼圆',fg="Blue3")
    w1.place(x=20, y=450)

    # 进度条
    c1 = Scale(top, from_=0, to=100, orient="horizontal", length=254, repeatinterval=1000, variable=v1, width=13,
               command=jd_scale, label="进度", showvalue='0', font='幼圆',fg="Blue3")
    c1.place(x=20, y=500)

    pb = Progressbar(top, length=260, mode='determinate', orient=HORIZONTAL)
    pb['maximum'] = 100
    pb['value'] = 0
    pb.place(x=20, y=550)

    # 绑定键盘
    top.bind('<space>', pa_un)

    # 右键菜单
    popupmenu = Menu(top, tearoff=False)
    demoStatus = BooleanVar()
    demoStatus1 = BooleanVar()
    demoStatus2 = BooleanVar()
    demoStatus.set(True)
    demoStatus1.set(False)
    demoStatus2.set(False)
    popupmenu.add_checkbutton(label='列表循环', command=normal, variable=demoStatus, font='幼圆')
    popupmenu.add_checkbutton(label='单曲循环', command=single_music, variable=demoStatus1, font='幼圆')
    popupmenu.add_checkbutton(label='随机播放', command=selectpath, variable=demoStatus2, font='幼圆')
    popupmenu.add_separator()
    popupmenu.add_command(label='本地文件播放', command=play, font='幼圆')
    popupmenu.add_command(label='切换背景图片', command=choosepic, font='幼圆')
    top.bind('<Button-3>', show_popupmenu)

    # 改变音量模式
    # Button(top, text="", command=gai_volume, height=0, bg='#b3b9db').place(x=20, y=450)
    # import threading
    # print(threading.active_count())
    # for thread in threading.enumerate():
    #     print(thread.name)
    top.protocol("WM_DELETE_WINDOW", close)
    top.mainloop()
