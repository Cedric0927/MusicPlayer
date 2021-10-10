from PyQt5.QtWidgets import QApplication, QMainWindow
from Project import MainWindow
import sys
import os
import pygame


class MyMainWindow(QMainWindow, MainWindow.Ui_Form):
    def __init__(self, parent=None):
        folder_path = r"D:\Graduation_Project\Music"
        folder_list = os.listdir(folder_path)  # 遍历文件夹里面每个文件
        self.listall = []
        self.listall_Backup = []
        self.relist = []
        self.re_fina = []
        # 下一首
        self.index = 0
        self.reindex = 0
        self.re_index = 0
        self.re_ou_index = 0
        self.love_index = -1.1
        count = 0
        for i in folder_list:  # 将文件夹里的文件按顺序传提给变量i  此处区别os.walk()
            if os.path.splitext(i)[1] == '.mp3':  # 提取特定后缀文件'.***'
                fil = folder_path + "\\" + i
                self.listall.append(fil)
                self.listall_Backup.append(fil)
                count += 1
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect()


    def playmusic(self):  # 开始播放
        global Musicname, Musicname1
        pygame.mixer.music.load(self.listall[0])
        pygame.mixer.music.play()
        Musicname = self.listall[0][28:-4]
        print(Musicname)
        Musicname1 = "        " + self.listall[0][28:-4]
        print(Musicname1)
        self.dagou()
        self.pbrun()

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

    def dagou(self):
        pass

    def pbrun(self):
        pass

    def play(self):  # 播放音乐
        try:
            f = self.callback()  # 选择制定文件
            f = f[0]
            pygame.mixer.music.load(f)
            pygame.mixer.music.play()
            global path, con
            con = 1
            path = f
            pathn.set(f)
        except IndexError:
            print('没有选择文件')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
