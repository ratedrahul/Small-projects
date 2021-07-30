from tkinter import *  
# from functools import partial
window = Tk()
window.title('Colors Rang-Birange')
from random import randint
from time import sleep



window.geometry('800x700')


def The_Color_Show(wait_time = 2.5,show_label =1):
	while True:

		a = hex(randint(0,255))[2:]
		if len(a)<2:
			a = '0'+a
		b = hex(randint(0,255))[2:]
		if len(b)<2:
			b = '0'+b
		c = hex(randint(0,255))[2:]
		if len(c)<2:
			c = '0'+c
		# print(a,b,c)
		color = '#'+a+b+c
	# # i = 99
	# 	y 
		window.config(bg = color)
		if show_label == 1:
			l = Label(window,text = color, font = ('LED',24,'bold'),bg = 'white')
			l.place(x = 320, y = 550)
		window.update()
		sleep(wait_time)

The_Color_Show()

