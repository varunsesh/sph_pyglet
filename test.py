import pyglet
from pyglet.window import key, mouse
from pyglet import shapes


x = 250
window = pyglet.window.Window()
batch = pyglet.graphics.Batch()
rectangle = shapes.Rectangle(x, 300, 400, 200, color=(255, 22, 20), batch=batch)
pos_x = 20
pos_y = window.height//2
speed = 100.0


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.LEFT:
        rectangle.x -= 10
    elif symbol == key.RIGHT:
        rectangle.x += 10
    elif symbol == key.UP:
        rectangle.y += 10
    elif symbol == key.DOWN:
        rectangle.y -= 10





@window.event
def on_draw():
    window.clear()
    circle = shapes.Circle(pos_x, pos_y, 20, color=(50, 225, 30), batch=batch)
    batch.draw()


def update(dt):
    global pos_x
    global pos_y
    pos_x += dt*speed
    pos_y += dt*speed
    print(pos_x, pos_y)
    
#event_logger = pyglet.window.event.WindowEventLogger()
#window.push_handlers(event_logger)


pyglet.clock.schedule_interval(update, 1/60)

pyglet.app.run()