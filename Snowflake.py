from turtle import *
from pynput import mouse

calc = 6
COLOR = "blue"
LEV = int(input("Введите количество уровней: "))
SIZE = int(input("Введите Размер фрактала: "))

for _ in range(LEV):
    calc *= 4
calc+=2
TRACER = calc

#speed(1)


def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def snowflake(size, levels):
    if levels == 0:
        forward(size)
        return
    size/=3
    go_inner(size, levels)

def go_inner(size, levels):
    draw_inner(size, levels-1)
    right(120)
    draw_inner(size, levels-1)

def draw_inner(size, levels):
    snowflake(size, levels)
    left(60)
    snowflake(size, levels)
    
def main():
    penup()
    tracer(TRACER,0)
    backward(SIZE/2)
    pendown()
    draw()

def draw():
    for _ in range(3):
        snowflake(SIZE, LEV)
        right(120)

def scroll(x, y, dx, dy):
    global SIZE
    SIZE += dy * 12.5
    draw()

    
listener = mouse.Listener(
    on_scroll=scroll)

listener.start()


main()
mainloop()