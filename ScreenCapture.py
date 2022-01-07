import os
import datetime
import shutil
import win32api,win32con,win32gui

def ScreenCapture():
    time2 = datetime.datetime.now().month
    time3 = datetime.datetime.now().day
    #print(time3, time2)
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
    if (win32gui.IsIconic(handle)) :
        win32gui.ShowWindow(handle, win32con.SW_RESTORE)
    else:
        win32gui.ShowWindow(handle, win32con.SW_RESTORE)
        win32gui.SetForegroundWindow(handle)



    # 设为高亮

    from PIL import Image, ImageGrab
    time_h = (datetime.datetime.now().hour)
    time_m = (datetime.datetime.now().minute)
    # 设置裕量
    overmeasure = 90
    # img_ready = ImageGrab.grab((x1 , y1 , x2 , y2 ))
    img_ready = ImageGrab.grab((x1 + 9.4 * overmeasure, y1+overmeasure, x2, y2 - 3.8*overmeasure))
    # 截图

    if (os.path.exists(path) == False):
        os.mkdir(path)
        img_ready.save(path + '\\' + str(time_h) + "-" + str(time_m) + '.jpg')
    else:
        img_ready.save(path + '\\' + str(time_h) + "-" + str(time_m) + '.jpg')
    shutil.copyfile(path + '\\' + str(time_h) + "-" + str(time_m) + '.jpg', "a.jpg")
    win32gui.ShowWindow(handle, win32con.SW_HIDE)


if __name__ == '__main__':
    ScreenCapture()