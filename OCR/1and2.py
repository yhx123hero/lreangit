#!/usr/bin/env python
# encoding: utf-8
'''
@author: yihuixiong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: 1and2.py
@time: 2019/3/2 10:41
@desc:
'''

import pyHook  # 钩子~
import pythoncom
from pykeyboard import PyKeyboard
import win32clipboard as wc #读取剪切板数据
import win32con
from threading import Timer
import time
from pymouse import PyMouse #获得当前鼠标信息
import Tkinter

currentData=''
time1= 0
time2 = 0

def transMousePosition():
    m = PyMouse()
    return "100x100+"+str(m.position()[0])+"+"+str(m.position()[1])
def Print(text):
    position = transMousePosition()  # 取得当前鼠标位置
    top = Tkinter.Tk()  # 窗口初始化
    top.wm_attributes('-topmost', 1)  # 置顶窗口
    top.geometry(position)  # 指定定位生成指定大小窗口
    e = Tkinter.Text()  # 生成文本框部件
    e.insert(1.0, text)  # 插入数据
    e.pack()  # 将部件打包进窗口
    top.mainloop()  # 进入消息循环

def getCopyText():
    wc.OpenClipboard()
    copy_text = wc.GetClipboardData(win32con.CF_UNICODETEXT)
    wc.CloseClipboard()
    global currentData
    if copy_text != currentData:
        currentData = copy_text
        print copy_text
        a = Timer(0.5,Print,(copy_text,))
        a.start()
    return copy_text


def mouse_event(event):
    k = PyKeyboard()
    if event.MessageName == 'mouse left down':
        global time1
        time1 = time.time()
    if event.MessageName == 'mouse left up':
        global time2
        time2 = time.time()
        if time2-time1 > 0.2:

            k.press_key(k.control_key)
            k.tap_key(67)
            k.release_key(k.control_key)
            t = Timer(0.5,getCopyText)
            t.start()
            return True
        return True
    return True




def main():
    hm = pyHook.HookManager()  # 创建一个钩子管理对象
    hm.MouseAll = mouse_event  # 监听所有鼠标事件
    hm.HookMouse()  # 设定鼠标钩子
    pythoncom.PumpMessages()  # 进入循环，程序一直监听


if __name__ == '__main__':
    main()


