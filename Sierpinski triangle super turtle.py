from matplotlib import *
import matplotlib.pyplot as plt
from functools import lru_cache

"""
Creates the Sierpinski triangle usingthe basic 
technique of getting the middle point of the line
"""

COLORMAP = [ "#CCCCFF","#9999FF", "#6666FF", "#3333FF",
            "#0000FF", "#0000CC", "#000099", "#000066", "#000033"]
#Blue palette
COLORMAP.reverse()

lev=int(input())
dots = []

def mouse_event(event): # click three times
    dots.append((event.xdata,event.ydata))
    if len(dots) == 3:
        print(dots)
        start()
        plt.show()

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
cid = fig.canvas.mpl_connect('button_press_event', mouse_event)

curr_level=0

@lru_cache()
def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)


def serpinsky(points, levels):
    
    draw (points, COLORMAP[levels%9])
    if levels > 0:
        serpinsky([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   levels-1)
        serpinsky([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   levels-1)
        serpinsky([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   levels-1)


def draw(points, colors):
    x = [points[0][0], points[1][0], points[2][0], points[0][0]]
    y = [points[0][1], points[1][1], points[2][1], points[0][1]]
    plt.plot(x, y,color=colors,  linewidth = '0.1' )
    plt.fill(x, y, color=colors)

@lru_cache()
def start():
    serpinsky(dots, lev)

plt.text(0.1, 0.9, "Выберите три точки для треугольника")
plt.show()

