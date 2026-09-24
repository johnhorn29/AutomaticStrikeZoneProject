# Use imports to create simple graphics with the lib.py file

from lib import *


x = 0
y = 0

def setup():
    pass

def draw():
    global x,y
    background(220,36,74)
    fill(20,77,145)
    stroke(0,255,255)
    rect(x,227,24,59)
    x+=1
    


run(setup, draw)