import turtle as t
import time as ti

def 画正方形(a):
    for i in range(4) :
        t.forward(a)
        t.left(90)
    t.done()
def 画圈(self, extent = None, steps = None):
    t.circle(self , extent , steps)
    t.done()

# def 画圈(r,s):
    # if s == None :
    #     t.circle(r)
    #     t.done()
    # elif s != None :
    #     t.circle(r,s)
    #     t.done()
def 画长方形(a,b):
    for i in range(2) :
        t.forward(a)
        t.left(90)
        t.forward(b)
        t.left(90)
    t.done()