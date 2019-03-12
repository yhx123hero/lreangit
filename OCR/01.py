#!/usr/bin/env python
# encoding: utf-8
'''
@author: yihuixiong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: 01.py
@time: 2019/3/9 22:59
@desc:
'''
import win32con,win32gui,win32api
import ctypes
class MyWindow():
    def __init__(self):
        self.getword_loaded = False
        #注册一个窗口类
        wc = win32gui.WNDCLASS()
        wc.lpszClassName = 'MyWindow'
        wc.hbrBackground = win32con.COLOR_BTNFACE+1
        wc.lpfnWndProc = self.wndProc
        class_atom=win32gui.RegisterClass(wc)
        #创建窗口
        self.hwnd = win32gui.CreateWindow(
            class_atom, u'窗口标题', win32con.WS_OVERLAPPEDWINDOW,
            win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT,
            200, 100,
            0,0, 0, None)
        #显示窗口
        win32gui.ShowWindow(self.hwnd, win32con.SW_SHOWNORMAL)
        self._init_getword()
    def _init_getword(self):
        LICENSEID = "{00000000-0000-0000-0000-000000000000}"
        MOUSEHOOK_CAPTURE_OK_MSG = "MOUSEHOOK_CAPTUREOK_MSG-" + LICENSEID
        self.MOUSEHOOK_CAPTURE_OK = win32gui.RegisterWindowMessage(MOUSEHOOK_CAPTURE_OK_MSG)
        self.icall = ctypes.windll.LoadLibrary('ICall')
        self.icall.SetMouseHook(self.hwnd)
        self.icall.MouseEnableCap(True)
        self.icall.GetWordEnableCap(True)
        self.getword_loaded = True
    def _del_getword(self):
        self.getword_loaded = False
        self.icall.RemoveMouseHook()
        hdll = win32api.GetModuleHandle('ICall.dll')
        win32api.FreeLibrary(hdll)
    def _capture_text(self):
        MAX_OUTPUT_LEN = 1024
        x,y = win32gui.GetCursorPos()
        hrwnd = self.icall.GetRealWindow(x, y)
        strtmp = ctypes.create_unicode_buffer('\0' * MAX_OUTPUT_LEN)
        i=ctypes.c_int(-1)
        ok = self.icall.GetWord(hrwnd, x, y, strtmp, MAX_OUTPUT_LEN, ctypes.byref(i))
        if ok:
            print u'全部文本:%s' % strtmp.value
            print u'单词位置:%s' % i.value
    #消息处理
    def wndProc(self, hwnd, msg, wParam, lParam):
        if self.getword_loaded and msg == self.MOUSEHOOK_CAPTURE_OK:
            print 'MOUSEHOOK_CAPTURE_OK'
            self._capture_text()
        if msg == win32con.WM_CLOSE:
            print 'WM_CLOSE'
            self._del_getword()
        if msg == win32con.WM_DESTROY:
            print 'WM_DESTROY'
            win32gui.PostQuitMessage(0)
        return win32gui.DefWindowProc(hwnd, msg, wParam, lParam)
mw = MyWindow()
win32gui.PumpMessages()
