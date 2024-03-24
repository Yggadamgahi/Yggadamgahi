from tkinter import *
#body
win = Tk()
win.title('calc for teacher amiry')
win.geometry('800x600')
win.maxsize(1024,768)
win.minsize(800,600)
#lable
lable = Label(win,text='this app create by yazdanghadamgahi',background='green',fg='yellow')
lable.pack()
#inputer
inp = Entry(win)
inp.pack()
#btn
def cli():
    x = eval(inp.get())
    lable.config(text=x)
    lable.pack()
btn = Button(win,text='show',background='green',fg='yellow',command=cli)
btn.pack()
#main
win.mainloop()
