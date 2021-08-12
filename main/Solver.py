from main.Vector2D import Vector2D
from main.Particle import Particle, ParticleManager
import math


class Solver():
    def __init__(self):
        self.pm = ParticleManager()



    def InitSPH(self, Re, height):
        number_particles = 16
    
        
        for y in range(0,height):
            for x in range(0,height):
                self.pm.addParticle(x,y,1.0)

        return self.pm.particleList




    def ComputeForces(self, Re, H):
        pass

    def UpdatePos(self):
        pass






    
    

