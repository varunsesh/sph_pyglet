import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np





class App:
    
    def __init__(self, particles, solver, lock, window_width=640, window_height=480):
        # Initialize Pygame and set up the OpenGL context
        pygame.init()
        screen = pygame.display.set_mode((int(window_width), int(window_height)), DOUBLEBUF | OPENGL)
        pygame.display.set_caption('SPH Particle Renderer')
        glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background color to white
        
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, window_width, 0, window_height, -1, 1)  # Set orthographic projection
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        self.particles = particles
        self.solver = solver
        self.lock = lock

        self.main_loop()

    # Function to render a circle at (x, y) with given radius
    def draw_circle(self, position, radius, color, segments=32):
        glColor3f(color[0], color[1], color[2])  # Set the color
        glBegin(GL_TRIANGLE_FAN)
        glVertex2f(position.x, position.y)
        for i in range(segments + 1):
            angle = 2.0 * np.pi * i / segments
            glVertex2f(position.x + np.cos(angle) * radius, position.y + np.sin(angle) * radius)
        glEnd()

    def pause(self):
        paused = True
        print("Paused. Press SPACE to resume.")
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_SPACE]:
                        paused = False
                        print("Resumed.")
                    if keys[pygame.K_ESCAPE]:
                        pygame.quit()
                        exit()
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            pygame.time.wait(100)
    
    def main_loop(self):
        # Main loop
        running = True
        while running:

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_ESCAPE]:
                        running = False
                    if keys[pygame.K_SPACE]:
                        self.pause()
                        print("Space key pressed")
                    print(f"Key pressed: {pygame.key.name(event.key)}")
                    

                if event.type == QUIT :
                    running = False

            glClear(GL_COLOR_BUFFER_BIT)
            with self.lock:
                for particle in self.particles:
                    self.draw_circle(particle.position, particle.radius, (0.0, 0.7, 1.0))
                    #compute forces on each particle
                    #update position
                    # above two done by solver

            pygame.display.flip()
            pygame.time.wait(33)  # ~30 FPS

        pygame.quit()
