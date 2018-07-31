import subprocess
import os
import random
import time


def get_screenshot(a):
    """获取手机截图,autojump.png"""
    process = subprocess.Popen('adb -s emulator-5556 shell screencap -p', shell = True, stdout = subprocess.PIPE)
    screenshot = process.stdout.read()
    screenshot = screenshot.replace(b'\r\n', b'\n')
    autoscreenshot = 'D:\\python_project\\fgo\\fgopic\\script\\act2\\auto_%s.png' %a
    with open(autoscreenshot, 'wb') as f:
        f.write(screenshot)
    #print(screenshot)
    with open('autojump.png', 'wb') as f:
        f.write(screenshot)

def run():
    global x
    h = 0
    while True:
        sourcepath = 'D:\\python_project\\fgo\\fgopic\\script\\auto_%s.png' %h
        if os.path.exists(sourcepath):
            # b = DHash(sourcepath)
            # x.append(b)
            h += 1

    
        else:
            wait = input('数字')
            get_screenshot(wait)    #自动截图存在对比图和 auto自动存图
            # get_screenshot()
            # c = DHash(r'D:\python_project\fgo\auto5556.png')   #算自动截图的hash值
            # f = Hamming_Distance(c) #对比Dhash值，并且用adb模拟按键
if __name__ == '__main__':
    run()