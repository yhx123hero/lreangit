#!/usr/bin/env python
# encoding: utf-8
from pynput.keyboard import Key, Controller
import time
from pynput.mouse import Button
from pynput import mouse
'''
@author: yihuixiong
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: deamoncao100@gmail.com
@software: garner
@file: new1.py
@time: 2019/3/9 10:58
@desc:
'''

'''
:param callable on_move: The callback to call when mouse move events occur.

        It will be called with the arguments ``(x, y)``, which is the new
        pointer position. If this callback raises :class:`StopException` or
        returns ``False``, the listener is stopped.

    :param callable on_click: The callback to call when a mouse button is
        clicked.

        It will be called with the arguments ``(x, y, button, pressed)``,
        where ``(x, y)`` is the new pointer position, ``button`` is one of the
        :class:`Button` values and ``pressed`` is whether the button was
        pressed.

        If this callback raises :class:`StopException` or returns ``False``,
        the listener is stopped.

    :param callable on_scroll: The callback to call when mouse scroll
        events occur.

        It will be called with the arguments ``(x, y, dx, dy)``, where
        ``(x, y)`` is the new pointer position, and ``(dx, dy)`` is the scroll
        vector.

        If this callback raises :class:`StopException` or returns ``False``,
        the listener is stopped.

    :param bool suppress: Whether to suppress events. Setting this to ``True``
        will prevent the input events from being passed to the rest of the
        system.
'''


global time1
time1 = 0


def on_move(x, y):
    print('Pointer moved to {o}'.format((x, y)))


def on_click(x, y, button, pressed):

    if pressed:
        if button == Button.left:
            global time1
            time1 = time.time()
    else:
        if button == Button.left:
            global time1

            if time.time() - time1 > 0.2:

                keyboard = Controller()
                keyboard.press(Key.ctrl.value)
                keyboard.press('c')
                keyboard.release('c')
                keyboard.release(Key.ctrl.value)


while True:
    with mouse.Listener(on_click=on_click, suppress=False) as listener:
        listener.join()
