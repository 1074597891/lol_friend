# 完成定时截图，然后读取文件，把文件转成文本，通过识别文本，正则提取获取好友信息

import datetime
import os
import time

import cv2
import ocr,ocr_high,ScreenCapture,open_txt,open_cv
from recover import recover


def main():
    while 1:
        if(os.path.exists("./log_in")=="True"):
            os.removedirs("./log_in")
            recover()
            break
        ScreenCapture.ScreenCapture()
        img = cv2.imread(r"./a.jpg", cv2.IMREAD_COLOR)
        open_cv.contrast_img1(img, 1.3, 100)

        # 开始识别通过普通精度和高精度
        time_m = (datetime.datetime.now().minute)
        if(time_m%10!=0):
            # opencv  模块  增加图片亮度
            ocr.baiduOCR('b.jpg')
            if (os.path.exists("./1.txt") == "True"):
                open_txt.trip()
        else:
            ocr_high.baiduOCR_high('b.jpg')
            if (os.path.exists("./1.txt") == "True"):
                open_txt.trip()
        time.sleep(9)
        # 推迟执行、休眠
if __name__ == '__main__':
    main()


