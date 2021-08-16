from main.Vector2D import Vector2D
from main.Particle import Particle, ParticleManager
import math


class Solver():
    def __init__(self):
        self.pm = ParticleManager()
        self.deltaT = 0.01



    def InitSPH(self, Re, height):
        number_particles = 16
        
        for y in range(0,height):
            for x in range(0,height):
                self.pm.addParticle(x,y,1.0)

        return self.pm.particleList




    def ComputeForces(self):
        F = Vector2D(100.0,100.0)
        return F

    def UpdatePos(self):
        F = self.ComputeForces()
        for p in self.pm.particleList:
            p.position = p.position +(p.velocity+F*self.deltaT)*self.deltaT
        
        return self.pm.particleList
            






    
    

