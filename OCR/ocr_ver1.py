#!/usr/bin/env python
# encoding: utf-8
'''
@author: yihuixiong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: ocr_ver3.py
@time: 2019/3/2 10:41
@desc:
'''

import pyHook  # 钩子~
import pythoncom
from pykeyboard import PyKeyboard
import win32clipboard as wc #读取剪切板数据
import win32con
from threading import _Timer
import time


class CustomTimer(_Timer):
    def __init__(self, interval, function, args=[], kwargs={}):
        self._original_function = function
        super(CustomTimer, self).__init__(interval, self._do_execute, args, kwargs)

    def _do_execute(self, *a, **kw):
        self.result = self._original_function(*a, **kw)

    def join(self):
        super(CustomTimer, self).join()
        return self.result


currentData=''
time1= 0
time2 = 0


def getCopyText():
    wc.OpenClipboard()
    copy_text = wc.GetClipboardData(win32con.CF_UNICODETEXT)
    wc.CloseClipboard()
    return copy_text

#返会是否有新的复制数据
def newCopyData():
    return cmp(currentData,str(getCopyText()))
# 监听键盘事件

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
            c = CustomTimer(0.5,getCopyText)
            c.start()
            print c.join()
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


