import colorsys
import json
import numpy as np
import vispy.scene
from vispy.scene import visuals

tresholds = { 'xmin': -2, 'xmax': 2, 'ymin': -2, 'ymax': 2, 'zmin': -2, 'zmax': 2}
width = height = depth = 150
max_iter = 50
power = 2

class Point3d:

    def __init__(self, x, y, z):
            self.x, self.y, self.z = x, y, z
    
    def getSpherical(self):
        r = np.sqrt(self.x**2 + self.y**2 + self.z**2)
        phi = np.arctan2(self.y , self.x)
        theta = np.arctan2(np.sqrt(self.x**2 + self.y**2), self.z)
        return r, phi, theta
    
    def toPower(self, power):
        r, phi, theta = self.getSpherical()
        nr = r**power
        cp = nr * np.sin(power * theta)
        self.x = cp * np.cos(power * phi)
        self.y = cp * np.sin(power * phi)
        self.z = nr * np.cos(power * theta)
        return self
        
    def add(self, other_point):
        self.x += other_point.x
        self.y += other_point.y
        self.z += other_point.z
        return self
    
    def isNotMandelbrot(self, radius):
        r, _, _ = self.getSpherical()
        return (r > radius)
    
def mandelbulb(x, y, z, max_iter, edge):
    point = Point3d(x, y, z)  
    r, _, _ = point.getSpherical()
    for _ in range(max_iter):
        if point.toPower(power).add(Point3d(x, y, z)).isNotMandelbrot(2):
            return [None,None,None], False, 0
    if not edge:
        return [x,y,z], True, r
    else:
        return [None,None,None], edge, 0

def mandelbulb_set(tresholds, width, height, depth, max_iter, color_array, rgb):    
    try:
        return read_from_file(str(power), str(depth), str(max_iter))
    except:
        pass
    
    result = np.full((width*height*depth,3 ), None)
    r = np.linspace(tresholds['xmin'], tresholds['xmax'], width)
    i = np.linspace(tresholds['ymin'], tresholds['ymax'], height)
    j = np.linspace(tresholds['zmin'], tresholds['zmax'], depth)
    
    dotnum=0
    for xi in r:
        for yi in i:
            edge = False
            for zi in j:
                re, edge, rr = mandelbulb(xi, yi, zi, max_iter, edge)
                result[dotnum] = re
                color_array[dotnum] = rgb[int(rr*100/2)]
                dotnum+=1

    return [result, color_array]

def plot_mandelbulb(result, color_array):
    canvas = vispy.scene.SceneCanvas(keys='interactive', show=True)
    view = canvas.central_widget.add_view()
    scatter = visuals.Markers()
    scatter.set_data(result, edge_width=0, face_color=color_array, size=3)
    view.add(scatter)
    view.camera = 'turntable' # or try 'arcball'

    if __name__ == '__main__':
        import sys
        if sys.flags.interactive != 1:
            vispy.app.run()
    
    write_to_file(str(power), str(depth), str(max_iter), [result.tolist(), color_array.tolist()])

def read_from_file(power, depth, maxiter):
    filename = "mandelbulb_"+power+"_"+depth+"_"+maxiter+".json"
    f = open(filename)
    j = json.loads(f.read())
    f.close
    return j

def write_to_file(power, depth, maxiter, data):
    filename = "mandelbulb_"+power+"_"+depth+"_"+maxiter+".json"
    f = open(filename, "w")
    f.write(json.dumps(data))
    f.close
    
color_array = np.full((width*height*depth,3 ), None)

hsv = [(h, 1, 1) for h in np.linspace(0, 2/3, 100)]
rgb = [colorsys.hsv_to_rgb(*tup) for tup in hsv]

ready = mandelbulb_set(tresholds, width, height, depth, max_iter, color_array, rgb)
result = np.array(ready[0])
color_array = np.array(ready[1])

plot_mandelbulb(result, color_array)

