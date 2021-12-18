
from aip import AipOcr
import webbrowser as web
import os
import time
import datetime


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
    path_time = ('1')
    path = ("F:\\Desktop\\ocr\\" + path_time)

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