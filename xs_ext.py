import turtle as t
import time

class xs海龟():
    def 画正方形(a):
        for i in range(4) :
            t.forward(a)
            t.left(90)
        t.done()

    def 画圈(self, extent = None, steps = None):
        t.circle(self , extent , steps)
        t.done()

    '''def 画圈(r,s):
        if s == None :
            t.circle(r)
            t.done()
        elif s != None :
            t.circle(r,s)
            t.done()
    '''

    def 画长方形(a,b):
        for i in range(2) :
            t.forward(a)
            t.left(90)
            t.forward(b)
            t.left(90)
        t.done()

'''def 转文本(byte):
    return 'str(byte)'

def 跳出循环():
    return 'break'

def 循环执行(frequency):
    return 'for i in range (frequency):+    '

无限循环 = 'while True:'''
def 打印(content):
    print(content)

def 导库(name) :
    return 'import {name}'

def 等待(s) :
    time.sleep(s)
