import numpy as np
import matplotlib.pyplot as plt

def plotJuliaSet(pixel, dot, maxiter):
    x, y = np.meshgrid(np.arange(-2, 2, pixel), np.arange(-2, 2, pixel))
    z = x + y * 1j
    c = dot* 1j  # Adjust this expression to define different Julia constants
    inSet = np.ones_like(z, dtype=bool)
    iterations = np.zeros_like(z, dtype=int)

    isJulia(maxiter, c, z, inSet, iterations)

    plt.imshow(iterations.T, cmap='plasma', extent=[-2, 2, -2, 2])
    
    plt.show()

def isJulia(maxiter, c, z, inSet, iterations):
    for _ in range(maxiter):
        z = z**2 + c
        inSet = np.logical_and(inSet, abs(z) <= 4)
        iterations[inSet] += 1

def on_scroll(event):
    global dot
    dot+=event.step/10
    print(dot)
    plotJuliaSet(pixel, dot, maxiter)

dot = float(input("Enter the dot for build: "))
pixel = 4 / (int(input("Enter the diameter in pixels: ")) - 1)
maxiter = int(input("Enter the maximum number of iterations: "))

plt.connect('scroll_event', on_scroll)

plotJuliaSet(pixel, dot, maxiter)