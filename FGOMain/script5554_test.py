import cv2
import numpy as np 
import subprocess
import os 
import random
import time

x = []

def get_screenshot():
    """获取手机截图,autojump.png"""
    process = subprocess.Popen('adb -s emulator-5554 shell screencap -p', shell = True, stdout = subprocess.PIPE)
    screenshot = process.stdout.read()
    screenshot = screenshot.replace(b'\r\n', b'\n')
    # autoscreenshot = 'D:\\python_project\\fgo\\fgopic\\script\\auto_%s.png' %a
    # with open(autoscreenshot, 'wb') as f:
    #     f.write(screenshot)
    with open(r'D:\python_project\fgo\auto5554.png','wb') as g:
        g.write(screenshot)
   # return f

def DHash(path):
    #img = cv2.imread(r'D:\python_project\fgo\autojump5554.png')
    img = cv2.imread(r'%s' %(path))
    #cv2.imshow('image', img)
    #cv2.waitKey(0)
    #1.得到图片缩略图的二维数组（灰度图）
    resize_width = 17
    resiez_height = 16
    smaller_img = cv2.resize(img,(resize_width,resiez_height))
    gray = cv2.cvtColor(smaller_img, cv2.COLOR_BGR2GRAY)

    #2，原数组美行右边的减去左边的
    gray_left = gray[:16,:16].copy().astype(np.float)
    gray_right = gray[:16,1:17].copy().astype(np.float)
    dhash_array = gray_right -gray_left
    dhash_array[dhash_array<0] = 0
    dhash_array[dhash_array>0] = 1
    dhash_array_one = list(dhash_array.flatten().astype(np.int)) #转化为一维数组在转化为整型在转化为列表
    decimal_value=0
    hash_string = ""
    index = 0
    for value in dhash_array_one:
        index += 1
        if value:
            decimal_value += value*(2**(index%8))
        if index % 8 ==7:
            hash_string += str(hex(decimal_value)[2:].rjust(2,'0'))  #hex形式为0xf ==>补全为 0x0f并取后两位
            decimal_value =0 
    print(hash_string)
    return hash_string

   # dhash_array
    #print(dhash_array_one)
    #print(type(dhash_array_one))
    #a=str(dhash_array_one).strip()
    #print(a)
    #print(gray_right.dtype)
    #print(gray_left.dtype)

    #gray_one = gray.flatten() #转化为一维数组
    #print(gray_one)
    #3.比较相邻像素
    #print(pixel)
def Hamming_Distance(c):
    global x
    e = []
    
        #c = r'D:\python_project\fgo\auto.png'
   # b = r'D:\python_project\fgo\fgopic\batchoose.png'
    #c = r'D:\python_project\fgo\fgopic\begbat.png'
    for value in x:
        difference = (int(c, 16)) ^ (int(value, 16))
        d = bin(difference).count('1')
        e.append(d)
    b = e.index(min(e))
    if b == 0 or b ==9 or b==21:
        print('找到了index =0，游戏刚开始')
        phone_cmd(970,1700,300,400)
        time.sleep(3)
    if b == 1 or b ==10:
        print('找到了index =1，step=1')
        phone_cmd(500,800,350,500)
        time.sleep(3)
        phone_cmd(1650,1700,995,1005)
        time.sleep(3)
    if b == 2 or b ==11:
        print('找到了index =2，step=2,停顿5S读图')
        phone_cmd(1730,1800,1000,1020)
        time.sleep(5)
    if b == 3 or b ==12:
        print('找到了index =3，step=3，选择attack项目')
        phone_cmd(1600,1700,850,950)
        time.sleep(3)
    if b == 4 or b ==13 or b ==19 or b ==20:
        print('找到了index =4，step=4，选择卡牌了，判断助战特异点')
        phone_cmd(1650,1700,995,1005)
        img = cv2.imread(r'D:\python_project\fgo\auto5554.png')
        img1 = img[633,224]
        img2 = img[633,708]
        img3 = img[633,1091]
        img4 = img[633,1477]
        img5 = img[633,1867]
        count =0 
        phone_cmd(510,725,300,350)
        phone_cmd(877,1092,300,350)
        phone_cmd(1244,1459,300,350)
        card_counta=0
        card_countb=0
        card_countc=0
        card_countd=0
        card_counte=0
        while count <3:
            if int(img1.min()) >230 and card_counta == 0:
                phone_cmd(96,280,640,880)
                card_counta += 1
            elif int(img2.min()) >230 and card_countb == 0:
                phone_cmd(500,650,640,880)
                card_countb += 1
            elif int(img3.min()) >230 and card_countc == 0:
                phone_cmd(870,1020,640,880)
                card_countc += 1
            elif int(img4.min()) >230 and card_countd == 0:
                phone_cmd(1300,1400 ,640,880)
                card_countd += 1
            elif int(img5.min()) >230 and card_counte == 0:
                phone_cmd(1680,1800,640,880)
                card_counte += 1
            elif card_counta == 0:
                phone_cmd(96,280,640,880)
                card_counta += 1
            elif card_countb == 0:
                phone_cmd(500,650,640,880)
                card_countb += 1
            elif card_countc == 0:
                phone_cmd(870,1020,640,880)
                card_countc += 1
            elif card_countd == 0:
                phone_cmd(1300,1400 ,640,880)
                card_countd += 1
            
            count += 1
        
        phone_cmd(1650,1700,995,1005)
        time.sleep(3)
    if b == 5:
        print('找到了index =5，step=5')
        phone_cmd(1730,1800,1000,1020)
        time.sleep(3)
    if b ==6:
        print('找到了index =6，step=6')
        phone_cmd(1730,1800,1000,1020)
        time.sleep(3)
    
    if b ==7:
        print('找到了index =7，step=7')
        phone_cmd(1730,1800,1000,1020)
        time.sleep(3)
    if b ==8:
        print('找到了index =8，step=8')
        phone_cmd(1730,1800,1000,1020)
        time.sleep(3)
    # if b ==9:
    #     print('找到了index =9，step=9')
    #     time.sleep(3)
    # if b ==10:
    #     print('找到了index =10，step=10')
    #     time.sleep(3)
    if b ==14 or b== 15 or b==16 or b==17:
        print('找到了index =14，step=14,剧情跳过')
        phone_cmd(1735,1835,37,87)
        time.sleep(3)
        phone_cmd(1150,1385,815,870)
        time.sleep(3)

    if b == 18:
        print('找到了index =18，step=18,剧情选择')
        phone_cmd(1400,1450,500,520)
        time.sleep(3)
    
    if b ==22:
        print('找到了index =22，step=22,申请好友')
        phone_cmd(1230,1600,900,950)
        time.sleep(3)

def phone_cmd(start_w,end_w,start_h,end_h):
    press_time = random.randint(10,80)
    a = random.randint(start_w,end_w)
    b = random.randint(start_h,end_h)
    cmd = 'adb -s emulator-5554 shell input swipe %d %d %d %d %d' % (a, b, a, b, press_time)
    os.system(cmd)
def run():
    global x
    h = 0
    while True:
        sourcepath = 'D:\\python_project\\fgo\\fgopic\\script\\auto_%s.png' %h
        if os.path.exists(sourcepath):
            b = DHash(sourcepath)
            x.append(b)
            h += 1
  
        else:
            #wait = input('数字')
            #get_screenshot(wait)    #自动截图存在对比图和 auto自动存图
            get_screenshot()
            c = DHash(r'D:\python_project\fgo\auto5554.png')   #算自动截图的hash值
            Hamming_Distance(c) #对比Dhash值，并且用adb模拟按键
if __name__ == '__main__':
    #get_screenshot()
    #DHash()
    #Hamming_Distance()
    run()