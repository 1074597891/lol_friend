import tkinter.messagebox
import webbrowser as web
import os
import time
def trip():
    root = tkinter.Tk()

    root.withdraw()
    list_ypd = []
    list_qm = []
    f_ypd = open("1.txt", "r")
    for lines in f_ypd.readlines():
        names_ypd = lines[:-1].split('\n')
        list_ypd.append(names_ypd)
    for nums in range(0, len(list_ypd)):
        if (((str(list_ypd[nums]) == "['挺哥无敌']") and str(list_ypd[nums + 1]) == "['在线']") or (
            (str(list_ypd[nums]) == "['挺哥无敌']") and str(list_ypd[nums + 1]) == "['游戏中']") or (
            (str(list_ypd[nums]) == "['挺哥无敌']") and str(list_ypd[nums + 1]) == "[队列中']") == 1):
            web.open('https://api.day.app/QFBnuUtQaSuxZns6Lz88eS/姚培栋上线了')
            tkinter.messagebox.showinfo('提示', '姚培栋上线了')
            os.mkdir("./log_in")
            time.sleep(5)
            os.system('taskkill /F /IM chrome.exe')


        elif (((str(list_ypd[nums]) == "['挺哥无敌、']") and str(list_ypd[nums + 1]) == "['在线']") or (
            (str(list_ypd[nums]) == "['挺哥无敌、']") and str(list_ypd[nums + 1]) == "['游戏中']") or (
            (str(list_ypd[nums]) == "['挺哥无敌、']") and str(list_ypd[nums + 1]) == "[队列中']") == 1):
            web.open('https://api.day.app/QFBnuUtQaSuxZns6Lz88eS/姚培栋上线了')
            tkinter.messagebox.showinfo('提示', '姚培栋上线了')
            os.mkdir("./log_in")
            time.sleep(5)
            os.system('taskkill /F /IM chrome.exe')
    f_ypd.close()

    f_qm = open("1.txt", "r")
    for lines1 in f_qm.readlines():
        names_qm = lines1[:-1].split('\n')
        list_qm.append(names_qm)
    for nums1 in range(0, len(list_qm)):
        if (((str(list_qm[nums1]) == "['不做出OPM不改名']") and str(list_qm[nums1 + 1]) == "['在线']") or (
                (str(list_qm[nums1]) == "['不做出OPM不改名']") and str(list_qm[nums1 + 1]) == "['游戏中']") or (
                (str(list_qm[nums1]) == "['不做出OPM不改名']") and str(list_qm[nums1 + 1]) == "[队列中']") == 1):
            web.open('https://api.day.app/QFBnuUtQaSuxZns6Lz88eS/乔梦上线了')
            tkinter.messagebox.showinfo('提示', '乔梦上线了')
            os.mkdir("./log_in")
            time.sleep(3)
            os.system('taskkill /F /IM chrome.exe')
        if(((str(list_qm[nums1]) == "['玩死你的是你爹']") and str(list_qm[nums1 + 1]) == "['在线']") or (
                (str(list_qm[nums1]) == "['玩死你的是你爹']") and str(list_qm[nums1 + 1]) == "['游戏中']") or (
                (str(list_qm[nums1]) == "['玩死你的是你爹']") and str(list_qm[nums1 + 1]) == "[队列中']") == 1):
            tkinter.messagebox.showinfo('提示', '小号上线了')
            os.mkdir("./log_in")
            time.sleep(3)
            os.system('taskkill /F /IM chrome.exe')
    f_qm.close()
    time.sleep(5)

if __name__ == '__main__':
    trip()

