#!/usr/bin/env python
# encoding: utf-8
'''
@author: yihuixiong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: 3.py.py
@time: 2019/3/5 20:43
@desc:
'''


import win32clipboard as wc #读取剪切板数据
from pymouse import PyMouse #获得当前鼠标信息
import Tkinter         #自带的GUI库，生成文本框
import time          #定时器，减少占用
import win32con
import sys
reload(sys)
sys.setdefaultencoding('utf8')
global currentData
currentData=''
global flag
flag = 0
#PyMouse得到的是2维字符串，但是tkinter生成窗体时需要的是类似（100*100+x+y）的字符串，100*100是窗口大小，xy是坐标点。
def transMousePosition():
    m = PyMouse()
    a , b = m.position()

    if a > 1000000:
        a= long(a - pow(2,32))
    return "150x150+"+str(a)+"+"+str(b)
#获得剪切板数据
def getCopyText():
    global currentData
    try:
        wc.OpenClipboard()
        copy_text = wc.GetClipboardData(win32con.CF_UNICODETEXT)
        wc.CloseClipboard()
    except:
        return currentData
    else:
        print copy_text
        return copy_text


def setText(aString):  # 写入剪切板
    wc.OpenClipboard()
    wc.EmptyClipboard()
    wc.SetClipboardData(win32con.CF_TEXT, aString)
    wc.CloseClipboard()

#返会是否有新的复制数据
#返会是否有新的复制数据
def Print(text):
    position = transMousePosition()  # 取得当前鼠标位置
    top = Tkinter.Tk()  # 窗口初始化
    top.bind('Ctrl-1')
    top.wm_attributes('-topmost', 1)  # 置顶窗口
    top.geometry(position)  # 指定定位生成指定大小窗口
    e = Tkinter.Text()  # 生成文本框部件
    e.insert(1.0, text)  # 插入数据
    e.pack()  # 将部件打包进窗口
    top.mainloop()  # 进入消息循环

def newCopyData():
    global currentData
    word = getCopyText()
    if cmp(currentData, word) != 0:
        return 1,word
    else:
        return 0,word

if __name__ == '__main__':
   # req_url = 'http://fanyi.youdao.com/translate'  # 创建连接接口，这里是有道词典的借口
    # 创建要提交的数据
    while 1:
        f , w = newCopyData()
        print f,w
        if f:
            global flag

            if flag > 0:
                global currentData
                currentData = w #取得当前剪切板数据
                if currentData!="":
                    Print(currentData)
            else:
                flag = flag + 1
        global currentData
        currentData = w
        time.sleep(0.1)
