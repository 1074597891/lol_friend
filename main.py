#!/usr/bin/env python
import os,time
#how to run it?
#nohup python -u example.py >> /data/logs/example.log 2>&1 &
while True:
        os.system('python bd_ai.py')
        #执行系统命令
        time.sleep(100)
        #推迟执行、休眠