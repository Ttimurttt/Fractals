""" Code generates Tree fractal with given level and 
"""
from turtle import *
from functools import lru_cache

colormode(1.0)

@lru_cache(typed=True)
def tree(tree_size, current_level, angle, str):
    if current_level == 0:
        return
    color((0.5, angle%360/360, current_level/LEVEL))
    forward(tree_size)
    right(angle)
    tree(tree_size*0.8, current_level - 1, angle, f"{str}right")
    left(angle*2)
    tree(tree_size*0.8 ,current_level - 1, angle, f"{str}left")
    right(angle)
    up()
    backward(tree_size)
    down()

def __main__():
    tracer(0,0)

    x=0
    levelscalc = sum(pow(2, levels) for levels in range(1, LEVEL))*12
    speed(0)
    left(90)
    up()
    goto(0, -200)
    down()
    width(5)

    while True:
        tree(SIZE, LEVEL, x, "straight")
        tracer(levelscalc,0)
        x +=1
        clear()

LEVEL = int(input("Введите уровень: "))
SIZE = int(input("Введите размер: "))

def scroll(x, y, dx, dy):
    global SIZE
    SIZE += dy * 12.5



     
__main__()