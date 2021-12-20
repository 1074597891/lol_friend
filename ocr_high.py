import os
from aip import AipOcr
def baiduOCR_high(picfile):
# picfile:图片文件名


    """ 你的 APPID AK SK """
    APP_ID = '23772553'
    API_KEY = 'U11QDtKOPFS7LalUp3ttcDYz'
    SECRET_KEY = 'psHywZdO2ZYlMPHakqxU6iznONej0wrP'


    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    i = open(picfile, 'rb')
    img = i.read()
    message = client.basicAccurate(img)

    i.close()

    # 输出文本内容
    for text in message.get('words_result'):  # 识别的内容
        a = text.get('words')
        with open('2.txt',"a+") as wfile:
            wfile.write(a)
            wfile.write('\n')
        print(a)

if __name__ == '__main__':
    baiduOCR_high('b.jpg')