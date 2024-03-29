from matplotlib.backend_bases import MouseButton
import numpy as np
import matplotlib.pyplot as plt

ax = plt.subplot()
coeff=4

def on_scroll(event):
    global maxiter
    global pixels
    pixels+=int(event.step*2)

def plotMandelbrotSet(maxiter, xright, xleft, yleft, yright):
    x, y = np.meshgrid(np.linspace(xright, xleft, pixels), np.linspace(yright, yleft, pixels))
    c = x + y * 1j
    z = np.zeros_like(c, dtype=complex)
    inSet = np.ones_like(c, dtype=bool)
    Boxes = np.zeros_like(c, dtype=int)
    
    isMandelbrot(maxiter, c, z, inSet, Boxes)
    
    plt.imshow(Boxes, cmap='plasma', extent = [xright, xleft, yleft, yright])
    plt.show()

def isMandelbrot(maxiter, c, z, inSet, Boxes):
    for _ in np.arange(maxiter):
        z = z**2 + c
        inSet = np.logical_and(inSet, abs(z) <= 2)
        Boxes[~inSet] += 1
            
def on_click(event):
    global coeff
    if event.button ==  MouseButton.LEFT:
        coeff*=1.2
    if event.button == MouseButton.RIGHT:
        coeff*=0.5
    plotMandelbrotSet(maxiter, event.xdata-coeff, event.xdata+coeff, event.ydata-coeff, event.ydata+coeff)

plt.connect('scroll_event', on_scroll)
plt.connect('button_press_event', on_click)
pixels = int(input("Введите диаметр в пикселях: "))
maxiter = int(input("Введите максимальное количество вычислений: "))

plotMandelbrotSet(maxiter,-2, 1, -2, 2)