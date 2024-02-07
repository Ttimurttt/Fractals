import matplotlib.pyplot as plt
from matplotlib import *
import numpy as np
from functools import lru_cache

start_dots = []
i = 100000 #int(input("Введите количество итераций: "))
pts_count = 3#int(input("Введите количество точек вашей фигуры"))

def mouse_event(event): # click three times
    start_dots.append([event.xdata,event.ydata])
    if len(start_dots) == pts_count:
        main()
        plt.show()

def calc( dot, p, length, last_corner):
    corner_to_go = np.random.choice(length, p=p)
    #while corner_to_go == last_corner:
    #    corner_to_go = np.random.choice(length, p=p)
    dot = (get_a_part(tuple(start_dots[corner_to_go]), tuple(dot), 2))
    return dot[0], dot[1], corner_to_go

#@lru_cache
def get_a_part(p1, p2, num):
    return [(p1[0] - p2[0])/num + p2[0], (p1[1] - p2[1])/num + p2[1]]

def main():
    global last_corner
    dots = start_dots[0]
    dotsx = []
    dotsy = []
    COLORMAP = ["red","green","blue","yellow","pink","black","orange",
                    "purple","beige","brown","gray","cyan","magenta"]
    colormap = []
    p = [1/pts_count for _ in range(pts_count)]
    length = len(start_dots)
    for _ in range(i):
        dotx, doty, last_corner = calc(tuple(dots), tuple(p), length, last_corner)
        dotsx.append(dotx)
        dotsy.append(doty)
        colormap.append(COLORMAP[last_corner])
        dots = [dotx, doty]
    plt.scatter(dotsx, dotsy, c=colormap, s = 1)

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
cid = fig.canvas.mpl_connect('button_press_event', mouse_event)
last_corner = 0
plt.plot(1, 1)
plt.show()