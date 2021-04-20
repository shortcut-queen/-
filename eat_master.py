# -*- coding: utf-8 -*-

__author__ = 'YIXUANLIU'
__date__ = '2021/04/19'
__version__ = 'V1.0'

import tkinter as tk
import tkinter.messagebox
import random


def random_dish():
    dish_list=['麻辣香锅','麻辣烫','火锅','冒菜','面条','米线','披萨','炸鸡','螺蛳粉','剁椒拌饭','饺子','抄手','盖饭','炒饭','日料','拌饭','部队锅','烤肉','烤冷面','臭豆腐','煎饼果子','黄焖鸡',
               '轻食','不吃','喝粥','烧烤','钵钵鸡','凉面','炒菜','烤肉拌饭','里脊饼','酸辣粉','鸭血粉丝汤','土豆粉','卤肉饭','抄手']
    len_dishlist=len(dish_list)
    num = random.randint(1, len_dishlist-1)
    result=dish_list[num]
    tkinter.messagebox.showinfo('结果',result)


root=tk.Tk()
root.title("今天吃什么")
root.geometry('500x300')
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
align='%dx%d+%d+%d' % (500, 300, (screenwidth - 500) / 2, (screenheight - 300) / 2)
root.geometry(align)
pic1=tk.PhotoImage(file="端碗.png")
pic2=tk.PhotoImage(file="吨吨吨.png")

img1label=tk.Label(root,justify=tk.LEFT,image=pic1,compound=tk.LEFT)
img2label=tk.Label(root,justify=tk.RIGHT,image=pic2,compound=tk.RIGHT)

b1=tk.Button(root,text='开始随机',font=('黑体',20),fg='#ff5546',width=8, height=3,command=lambda:random_dish())
b1.pack()
img1label.pack(side=tk.LEFT)
img2label.pack(side=tk.RIGHT)
root.mainloop()