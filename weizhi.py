#!/usr/bin/python
#coding:utf-8
#auth:Devotes

import pyautogui


pyautogui.FAILSAFE = True
currentMouseX,currentMouseY = pyautogui.position()
print currentMouseX,currentMouseY