import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet import shapes

from main.Solver import Solver
import math


####List of Global Constants
deltaT = 0.01
tfinal = 1.0
H = 16.0 # Parameter for kernel function influence
HSQ = H*H
height_dam = 4
grav = 9.81
nu = 0.8927
Re = height_dam*math.sqrt(grav*height_dam)/nu
rho0 = 1.0
k = 1.0
## Variables needed for rendering
position = []
circle = []
scale = 25
r = 10


##Creating an OpenGL context
window = pyglet.window.Window(caption = "SPH")
batch = pyglet.graphics.Batch()

fps_display = pyglet.window.FPSDisplay(window=window)



def get_postions(x,y):
    global position
    t = 0.5
    if len(position)>15:
        position = []
    position.append((x,y))

@window.event
def on_draw():
    global circle
    window.clear()
    for i in range(len(position)):
        if len(circle)>len(position):
            circle = []
        circle.append(shapes.Circle(scale*position[i][0], scale*position[i][1], r, color=(50, 225, 30), batch=batch))
        
    batch.draw()
    fps_display.draw()


def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step




def update(dt, solver):
    ##Update particle positions
    p_list = solver.update_pos()
    for p in p_list:
        get_postions(p.position.x, p.position.y)



event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)

if __name__=="__main__":
    solver = Solver(HSQ, rho0, k)
   
    particles = solver.init_sph(Re, height_dam)
        
    
    pyglet.clock.get_fps()
    pyglet.clock.schedule_interval(update, 1/60, solver)

    pyglet.app.run()

