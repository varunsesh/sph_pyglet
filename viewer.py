import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet import shapes



from main.Solver import Solver
import math

window = pyglet.window.Window()
batch = pyglet.graphics.Batch()
position = []
circle = []

@window.event
def on_key_press(symbol, modifiers):
    if symbol==key.A:
        print("Key A was pressed")
    elif symbol==key.ENTER:
        print("Key Enter was pressed")

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print("Left click")

def get_postions(x,y):
    global position
    t = 0.5
    position.append((x+t,y+t))
    


@window.event
def on_draw():
    r = 10
    scale = 50   
    for i in range(len(position)):
        circle.append(shapes.Circle(scale*position[i][0], scale*position[i][1], r, color=(50, 225, 30), batch=batch))
        circle[-1].opacity = 120
    window.clear()
    batch.draw()



event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)

if __name__=="__main__":
    solver = Solver()
    deltaT = 0.01
    tfinal = 1.0
    H = 16.0 # Parameter for kernel function influence
    HSQ = H*H
    height_dam = 4
    grav = 9.81
    nu = 0.8927
    Re = height_dam*math.sqrt(grav*height_dam)/nu
    particles = solver.InitSPH(Re, height_dam)
    
    for i in range(len(particles)):
        get_postions(particles[i].position.x, particles[i].position.y)
    
    pyglet.app.run()

