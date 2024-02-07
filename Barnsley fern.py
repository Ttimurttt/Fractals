import matplotlib.pyplot as plt
import numpy as np
import time

def calculate_next_point1(point):
    return .0, 0.16*point[1]

def calculate_next_point2(point):
    return 0.85*point[0] + 0.04*point[1], (-0.04*point[0] + 0.85 * point[1]) + 1.6

def calculate_next_point3(point):
    return 0.2*point[0] - 0.26*point[1], (0.23*point[0] + 0.22 * point[1]) + 1.6

def calculate_next_point4(point):
    return -0.15*point[0] + 0.28*point[1], (0.26*point[0] + 0.24*point[1]) + 0.44

def main(i):
    x, y = 0, 0
    ax = plt.axes()
    ax.set_facecolor("black")
    functions = [calculate_next_point1, calculate_next_point2, calculate_next_point3, calculate_next_point4]
    for iter in range(i):
        function = np.random.choice(functions, p=[0.01, 0.85, 0.07, 0.07])
        x, y = function ([x, y])
        dotsx[iter] = x
        dotsy[iter] = y

i = int(input("Введите количество итераций: "))
start = time.time()
dotsx = np.zeros(i)
dotsy = np.zeros(i)
main(i)

plt.scatter(dotsx, dotsy, s = 1, color = "white")
end = time.time()
print(end - start)
plt.show()


