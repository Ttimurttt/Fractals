import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pyautogui
i = 0
fig, ax = plt.subplots()
coeff = 1
pixels = int(input("Enter the diameter in pixels: "))
maxiter = int(input("Enter the maximum number of iterations: "))
ani = None
folder_path = r'C:\Users\talgu\Documents\Fractals\.venv\Frames\''

def plotMandelbrotSet(maxiter, xright, xleft, yleft, yright):
    x, y = np.meshgrid(np.linspace(xright, xleft, pixels), np.linspace(yright, yleft, pixels))
    c = x + y * 1j
    z = np.zeros_like(c, dtype=complex)
    inSet = np.ones_like(c, dtype=bool)
    Boxes = np.zeros_like(c, dtype=int)

    isMandelbrot(maxiter, c, z, inSet, Boxes)

    return Boxes

def isMandelbrot(maxiter, c, z, inSet, Boxes):
    for _ in np.arange(maxiter):
        z = z**2 + c
        inSet = np.logical_and(inSet, abs(z) <= 4)
        Boxes[~inSet] += 1

def update(event):
    global coeff, i
    x = event.xdata
    y = event.ydata
    ax.clear()
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginary')
    coeff *= 0.99  #-0.34831493420245574, -0.34853774148008254,-0.6065922085831237, -0.606486596104741
    xright = -1.7492086 - coeff
    xleft = -1.7492086 + coeff
    yleft = 0 - coeff
    yright = 0 + coeff

    Boxes = plotMandelbrotSet(maxiter, xright, xleft, yleft, yright)

    im = ax.imshow(Boxes, cmap='magma', extent=[xright, xleft, yleft, yright])
    i+=1
    filename = f'screenshot_{i}.png'  # Construct the filename based on the current iteration
    file_path = folder_path + filename  # Create the full file path
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(file_path)

    return [im]

def on_click(event):
    global coeff, ani
    if ani is not None:
        ani.event_source.stop()
    ani = animation.FuncAnimation(fig, update, frames=[event], interval=200)

    plt.show()

plt.connect('button_press_event', on_click)

# Initial frame
plt.imshow(plotMandelbrotSet(maxiter, -2, 2, -2, 2), cmap = "magma", extent=[-2, 2, -2, 2]) 
plt.show()
