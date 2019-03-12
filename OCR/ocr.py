#!/usr/bin/env python
# encoding: utf-8
'''
@author: yihuixiong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: ocr.py
@time: 2019/2/28 16:23
@desc:
'''
# codingutf-8
import inspect
import win32api
import os
from PIL import ImageGrab, Image
import pyHook  # 钩子~
import pythoncom
import pytesseract  # 图像识别文字包
import pyperclip

# 创建一个坐标列表
coordinate = [1.0, 1.0, 1.0, 1.0]


# 监听键盘事件
def on_mouse_event(event):
    # 获取当前文件路径
    file_ = inspect.getfile(inspect.currentframe())
    dir_path = os.path.abspath(os.path.dirname(file_))
    file_path = dir_path + 'read.jpg'
    # 监听鼠标事件
    if event.MessageName == 'mouse left down':
        coordinate[0:2] = event.Position
    elif event.MessageName == 'mouse left up':
        coordinate[2:4] = event.Position
        win32api.PostQuitMessage()  # 退出监听循环
        # 截取坐标图片

        pic = ImageGrab.grab(coordinate)
        print 1
        pic.save(file_path)
        print 1
        #text = pytesseract.image_to_string(Image.open(file_path), lang='chi_sim')  # 识别并返回
        text = pytesseract.image_to_string(pic, lang='chi_sim')  # 识别并返回
        print (text)
        pyperclip.copy(text.replace(' ', ''))  # 将识别内容导入系统剪切板
    return True


if __name__ == '__main__':
    hm = pyHook.HookManager()  # 创建一个钩子管理对象
    hm.MouseAll = on_mouse_event  # 监听所有鼠标事件
    hm.HookMouse()  # 设定鼠标钩子
    pythoncom.PumpMessages()  # 进入循环，程序一直监听