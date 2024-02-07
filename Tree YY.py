""" Code generates Tree fractal with given level and angle
"""
from turtle import *
from pynput import mouse



def tree(tree_size, current_level, angle):
    if current_level == 0:
        return
    color((0.5, angle%360/360, current_level/LEVEL))
    forward(tree_size)
    right(angle)
    tree(tree_size*0.8, current_level - 1, angle)
    left(angle*2)
    tree(tree_size*0.8 ,current_level - 1, angle)
    right(angle)
    up()
    backward(tree_size)
    down()

def __main__():
    tracer(0,0)
    colormode(1.0)
    
    listener.start()
    
    x=0
    levelscalc = sum(pow(2, levels) for levels in range(1, LEVEL))*12
    speed(0)
    
    left(90)
    up()
    goto(0, -200)
    down()
    width(5)
    tracer(levelscalc,0)
    tree(SIZE, LEVEL, x)
    x+=1
    tracer(levelscalc,0)
    
    while True:
        tree(SIZE, LEVEL, x)
        tracer(levelscalc,0)
        x +=1
        clear()

LEVEL = int(input("Введите уровень: "))
SIZE = 125

def scroll(x, y, dx, dy):
    global SIZE
    SIZE += dy * 12.5

listener = mouse.Listener(
    on_scroll=scroll)

__main__()
mainloop()