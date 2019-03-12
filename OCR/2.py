#!/usr/bin/env python
# encoding: utf-8
'''
@author: yihuixiong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: ocr_ver1.py
@time: 2019/3/1 17:34
@desc:
'''
import urllib #http连接需要用到
import json  #解析网页数据用
import win32clipboard as wc #读取剪切板数据
from pymouse import PyMouse #获得当前鼠标信息
import Tkinter         #自带的GUI库，生成文本框
import time          #定时器，减少占用
import sys
reload(sys)
sys.setdefaultencoding('utf8')
currentData=''

#PyMouse得到的是2维字符串，但是tkinter生成窗体时需要的是类似（100*100+x+y）的字符串，100*100是窗口大小，xy是坐标点。
def transMousePosition():
    m = PyMouse()
    return "100x100+"+str(m.position()[0])+"+"+str(m.position()[1])
#获得剪切板数据
def getCopyText():
    wc.OpenClipboard()
    copy_text = wc.GetClipboardData()
    wc.CloseClipboard()
    return copy_text
#返会是否有新的复制数据
def Print(text):
    position = transMousePosition()  # 取得当前鼠标位置
    top = Tkinter.Tk()  # 窗口初始化
    top.wm_attributes('-topmost', 1)  # 置顶窗口
    top.geometry(position)  # 指定定位生成指定大小窗口
    e = Tkinter.Text()  # 生成文本框部件
    e.insert(1.0, text)  # 插入数据
    e.pack()  # 将部件打包进窗口
    top.mainloop()  # 进入消息循环

def newCopyData():
    return cmp(currentData,str(getCopyText()))
if __name__ == '__main__':
    req_url = 'http://fanyi.youdao.com/translate'  # 创建连接接口，这里是有道词典的借口
    # 创建要提交的数据
    currentData=str(getCopyText())
    Form_Date = {}
    Form_Date['doctype'] = 'json'
    while 1:
        if newCopyData():
            currentData=str(getCopyText())#取得当前剪切板数据
            print(currentData)
            Form_Date['i'] = currentData # 传递数据
            data = urllib.urlencode(Form_Date).encode('utf-8') #数据转换
            response = urllib.urlopen(req_url, data) #提交数据并解析
            html = response.read().decode('utf-8')  #服务器返回结果读取
            translate_results = json.loads(html)  #以json格式载入
            translate_results = translate_results['translateResult'][0][0]['tgt']  # json格式调取
            print type(translate_results)
            Print(translate_results)
        currentData=str(getCopyText())
        time.sleep(1)
