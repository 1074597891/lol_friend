# 完成定时截图，然后读取文件，把文件转成文本，通过识别文本，正则提取获取好友信息
from typing import TextIO

from aip import AipOcr
import webbrowser as web
import os
import time
import datetime
import win32api,win32con,win32gui



""" 你的 APPID AK SK """
APP_ID = '23772553'
API_KEY = 'U11QDtKOPFS7LalUp3ttcDYz'
SECRET_KEY = 'psHywZdO2ZYlMPHakqxU6iznONej0wrP'
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 便利目录下所有文件

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
options = {
    'detect_direction': 'false',
    'language_type': 'CHN_ENG',
    "detect_language": 'false',
    'probability':'true'
}


if __name__ == '__main__':

    time2 = datetime.datetime.now().month
    time3 = datetime.datetime.now().day
    print(time3, time2)
    path_time = ("2021-0" + str(time2) + '-' + str(time3))
    path = ("D:\\ScreenCapture\\" + path_time)



    def get_window_pos(name):
        name = name
        handle = win32gui.FindWindow(0, name)
        # 获取窗口句柄
        if handle == 0:
            return None
        else:
            return win32gui.GetWindowRect(handle), handle


    (x1, y1, x2, y2), handle = get_window_pos('league of legends')

    # 其中窗口信息(x1, y1, x2, y2)，(x1, y1)是窗口左上角的坐标，(x2, y2)是窗口右下角的坐标。

    text = win32gui.SetForegroundWindow(handle)
    win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
    # 发送还原最小化窗口的信息
    win32gui.SetForegroundWindow(handle)

    # 设为高亮
    time.sleep(5)
    from PIL import Image, ImageGrab
    time_h = (datetime.datetime.now().hour)
    time_m = (datetime.datetime.now().minute)
    # 设置裕量
    overmeasure = 90

    img_ready = ImageGrab.grab((x1 + 12*overmeasure, y1 + 0.5 * overmeasure, x2 + 3.5 * overmeasure, y2 - 3 * overmeasure))
    # 截图
    print(os.path.exists(path))
    if (os.path.exists(path)== False):
        os.mkdir(path)
        img_ready.save(path + '\\' + str(time_h) + "-" + str(time_m) + '.jpg')
    else:
        img_ready.save(path + '\\' + str(time_h) + "-" + str(time_m) + '.jpg')



    filelist = os.listdir(path)
    for jpg in filelist :
        print (jpg)
        print (filelist)
        filepath = (path+'\\'+jpg)
        print (filepath)
        result = aipOcr.general(get_file_content(filepath), options)
        try:
            words_result = result['words_result']
            with open('1.txt', 'w') as file:
                for n in range(len(words_result)):
                    print(words_result[n]['words'])
                    file.write(words_result[n]['words'] + ';')
                file.write('\n')


        except:
            pass

        f = open("1.txt", "r")
        for lines in f.readlines():

            print(lines)
            names_ypd = lines[:-1].split(';')
            for nums in range(len(names_ypd)):
                if (((names_ypd[nums] == '挺哥无敌、') and (names_ypd[nums + 1] == '离线') == 1)):
                    web.open('http://192.168.1.4:8080/84nELEN5DY2vENgKcLHmmL/东子上线了?sound=minuet')





