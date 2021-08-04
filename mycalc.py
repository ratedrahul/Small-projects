from tkinter import *
import tkinter.messagebox
from time import sleep
from tkinter import Image, PhotoImage

window = Tk()
window.title('Calculator')
window.geometry('500x650')
pic = PhotoImage(file = 'calc.png')
start_point = 0
p1 = Label(window,image = pic )
p1.pack(side = TOP)

font = ('TimesNow 20 bold')
I1= Label(window, text = 'Calculator',font = font)
I1.pack()

E = Entry(window,font = font,justify = RIGHT)
E.pack(pady = 10)
memory = 0
f1 = Frame(window)
f1.pack(side = TOP,pady = 45)
def fn(event):
	b = event.widget
	text = b['text']
	if start_point == 0:
		E.insert(END,text)
	else:
		E.delete(0,END)
		# print('deleting e ')
		E.insert(END,text)


def eq(event):
	exp = E.get()
	try:
		ans= eval(exp)
	except Exception as er2:
		# tkinter.messagebox.showerror('Error ',er2)
		E.delete(0,END)
		E.insert(0,'invalid syntax')

	else:
		E.delete(0,END)
		E.insert(0,ans)
	start_point = 1
def clrr(event):
	E.delete(0,END)
def bac(event):
	Ex = E.get()
	Ex = Ex[0:len(Ex)-1]
	E.delete(0,END)
	E.insert(0,Ex)
def mem(event):
	global memory
	value = E.get()
	memory = int(memory)+int(value)
	E.delete(0,END)
	E.insert(0,memory)
	return memory
def M_show(event):
	an = mem(event)
count = 0
for i in range(3):
	for j in range(3):
		# if j < 3 and i<3:
		count+=1
		btn = Button(f1,text = count,font = font,width = 4,height = 1)
		btn.grid(row = i, column = j,padx = 2,pady = 2)
		btn.bind('<Button-1>',fn)
		# else:
plus = Button(f1,text = '+',font = font ,width = 4, height = 1)
plus.bind('<Button-1>',fn)
plus.grid(row = 0,column = 3)

minus = Button(f1,text = '-',font = font ,width = 4, height = 1)
minus.bind('<Button-1>',fn)
minus.grid(row = 1,column = 3)

mult = Button(f1,text = '*',font = font ,width = 4, height = 1)
mult.bind('<Button-1>',fn)
mult.grid(row = 2,column = 3)

div = Button(f1,text = '/',font = font ,width = 4, height = 1)
div.bind('<Button-1>',fn)
div.grid(row = 3,column = 3)
m = Button(f1,text = 'M+',font = font ,width = 4, height = 1)
m.bind('<Button-1>',mem)
m.grid(row = 3,column = 2)


dot = Button(f1,text = '.',font = font ,width = 4, height = 1)
dot.bind('<Button-1>',fn)
dot.grid(row = 3,column = 0)
zero = Button(f1,text = '0',font = font ,width = 4, height = 1)
zero.bind('<Button-1>',fn)
zero.grid(row = 3,column = 1)
clr = Button(f1,text = 'AC',font = font,width = 4)
clr.bind('<Button-1>',clrr)
clr.grid(row = 4,column = 0,pady = 5)

back = Button(f1,text = '<--',font = font,width = 4)
back.bind('<Button-1>',bac)
back.grid(row = 4,column = 1)

Equal = Button(f1,text = '=',font = font,width = 4)
Equal.bind('<Button-1>',eq)
Equal.grid(row = 4, column = 2)


M = Button(f1,text = 'M',font = font,width = 4)
M.bind('<Button-1>',M_show)
M.grid(row = 4, column = 3)

		# 	btn = Button(f1,text = liss[c],font = font,width = 4,height = 1)
		# 	btn.grid(row = i, column = j,padx = 2,pady = 2)
		# 	c+=1

# def eva():
# 	iii = ii.get()
# 	ans = eval(iii)
# 	print(ans)
# 	 ans
# MB = Button(text = 'Evaluate',font = font,command = eva)
# MB.pack()






###################################################################
scFrame = Frame(window)
sideFrame = Frame(window)



def cli(event):
	v = event.widget
	t = v['text'] 
	print(t)
	if t == 'Sqrt':
		value =int(E.get())
		import math
		ans = math.sqrt(value)
		E.delete(0,END)
		E.insert(0,ans)
		# print(ans)
	



sqrt = Button(scFrame,text = 'Sqrt',font = font,width = 4,pady = 2)
sqrt.bind('<Button-1>',cli)
sqrt.grid(row = 0, column = 0)
powBtn = Button(scFrame,text = 'powBtn',font = font,width = 4,padx = 2)
powBtn.bind('<Button-1>',cli)
powBtn.grid(row = 0, column = 1)

perc = Button(scFrame,text = '%',font = font,width = 4,padx = 2)
perc.grid(row = 0,column = 2)

Rnd = Button(scFrame,text = 'Rnd',font = font,width = 4,padx = 2)
Rnd.grid(row = 0 ,column = 3)
# c = Checkbutton(scFrame,text = 'bc ',font = font,width = 4)
# c.grid(row)
sin = Button(scFrame,text = 'sin',font = font,width = 4,padx = 2)
sin.grid(row = 1 ,column = 0)
cos = Button(scFrame,text = 'cos',font = font,width = 4,padx = 2)
cos.grid(row = 1 ,column = 1)
tan = Button(scFrame,text = 'tan',font = font,width = 4,padx = 2)
tan.grid(row = 1 ,column = 2)

mod = Button(scFrame,text = 'mod',font = font,width = 4,padx = 2)
mod.grid(row = 1 ,column = 3)

eq = Button(sideFrame,text = 'eq',font = font,width = 4,padx = 2)
eq.grid(row = 0 ,column = 0)
xf = Button(sideFrame,text = 'x!',font = font,width = 4,padx = 2)
xf.grid(row = 1 ,column = 0)
cube = Button(sideFrame,text = 'x^3',font = font,width = 4,padx = 2)
cube.grid(row = 2 ,column =0)

mod = Button(scFrame,text = 'mod',font = font,width = 4,padx = 2)
mod.grid(row = 1 ,column = 3)


normalcalc = True
def sc_click():
	global normalcalc
	if normalcalc:
		f1.pack_forget()
		scFrame.pack(side = TOP,pady= 10)
		sideFrame.pack(side= RIGHT)
		f1.pack(side = TOP)
		window.geometry('500x750')
		print('Show sc')
		normalcalc = False
	else:
		print('show normal')
		scFrame.pack_forget()
		# f1.pack(side = TOP)

		normalcalc = True




















menubar = Menu(window)
mode = Menu(menubar,tearoff = 0)
mode.add_checkbutton(label= 'Scientific', command = sc_click)
menubar.add_cascade(label = "Mode",menu = mode)
window.config(menu = menubar)

# menubar2 = Menu(window)
# exit = Menu(menubar)
# exit.add_command(label = 'Exit')
# window.config(menu = menubar2)
def Quit():
	exit()

bu = Button(window, text = 'Quit',font = font,command = Quit,bg = 'dark red')
bu.pack(side = BOTTOM)

