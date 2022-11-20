import turtle as t
import time

class xsturtle():
    def square(a,b):
        if b == None :
            for i in range(4) :
                t.forward(a)
                t.left(90)
            else:
                for i in range(2) :
                    t.forward(a)
                    t.left(90)
                    t.forward(b)
                    t.left(90)
            t.done()

    def circle(self, extent = None, steps = None):
        t.circle(self , extent , steps)
        t.done()

    '''def circle(r,s):
        if s == None :
            t.circle(r)
            t.done()
        elif s != None :
            t.circle(r,s)
            t.done()
    '''

#     def 画长方形(a,b):
#         for i in range(2) :
#             t.forward(a)
#             t.left(90)
#             t.forward(b)
#             t.left(90)
#         t.done()
    def triangle(a,d):
        t.forward(a)
        t.left(d)
        t.forward(a)
        t.goto(0,0)
        t.done()
    def forward(distance):
        t.forward(distance)
    def right(degree):
        t.right(degree)
    def left(degree):
        t.left(degree)
    def goto(x,y):
        t.goto(x,y)
    def clear():
        t.clear()
    def bgcolor():
        t.bgcolor()
    def 抬笔():
        t.penup()
# '''def 转文本(byte):
#     return 'str(byte)'

# def 跳出循环():
#     return 'break'

# def 循环执行(frequency):
#     return 'for i in range (frequency):+    '

# 无限循环 = 'while True:'''
# def 打印(content):
#     print(content)

# def 导库(name) :
#     return 'import {name}'

def wait(s) :
    time.sleep(s)

