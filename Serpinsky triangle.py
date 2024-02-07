from turtle import *

Screen().colormode(255)

COLORMAP = [(204, 204, 255), (153, 153, 255), (102, 102, 255), (51, 51, 255),
            (0, 0, 255), (0, 0, 204), (0, 0, 153), (0, 0, 102), (0, 0, 51)]
#Blue palette
COLORMAP.reverse()

speed(0)
lev=int(input())
up()
dots = []

def position(x, y):
    dots.append((x, y))
    # Store positions as tuples
    if len(dots) == 3:
        print(dots)
        onscreenclick(None)
        start()

tracer(0, 0)
width(1)
curr_level=0

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

def draw(points, color):
    fillcolor(color)
    up()
    goto(points[0][0], points[0][1])
    down()
    begin_fill()
    goto(points[1][0], points[1][1])
    goto(points[2][0], points[2][1])
    goto(points[0][0], points[0][1])
    end_fill()

def start():
    serpinsky(dots, lev)

while True:
    onscreenclick(position)
    mainloop()