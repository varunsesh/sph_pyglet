import pyglet
from pyglet.window import key
from pyglet.window import mouse
from pyglet import shapes



window = pyglet.window.Window()
batch = pyglet.graphics.Batch()



@window.event
def on_key_press(symbol, modifiers):
    if symbol==key.A:
        print("Key A was pressed")
    elif symbol==key.ENTER:
        print("Key Enter was pressed")
    
r = 100   
circle1=shapes.Circle(320,320, r, color=(50, 225, 30), batch=batch)
circle1.opacity = 120

@window.event
def on_draw():
    window.clear()
    batch.draw()



event_logger = pyglet.window.event.WindowEventLogger()
window.push_handlers(event_logger)


pyglet.app.run()