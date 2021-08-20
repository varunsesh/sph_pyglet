from main.Vector2D import Vector2D
from main.Particle import Particle, ParticleManager
import math


class Solver():
    

    def __init__(self, H, rho0, k):
        self.pm = ParticleManager()
        self.deltaT = 0.01
        self.H = H
        self.rho0 = rho0
        self.k = k
        self.HSQ = self.H*self.H
        self.__kernel_constant = 315/(1*math.pi*pow(H, 9.0))



    def init_sph(self, Re, height):
        number_particles = 16
        
        for y in range(0,height):
            for x in range(0,height):
                self.pm.addParticle(x,y,1.0)

        return self.pm.particleList


    def compute_forces(self):
        F = Vector2D(100.0,100.0)
        return F

    ## Using Poly6 Kernel Function
    def compute_density_pressure(self):
        r = Vector2D(0.0, 0.0)
        for pi in self.pm.particleList:
            pi.rho = 0.0
            for pj in self.pm.particleList:
                r2 = (r.distance_to(pj.position, pi.position))**2
                if (r2<self.HSQ):
                    pi.rho += 1*self.__kernel_constant*(self.HSQ-r2)**3
            pi.p = self.k*pi.rho - self.rho0


    def update_pos(self):
        F = self.compute_forces()
        for p in self.pm.particleList:
            p.position = p.position +(p.velocity+F*self.deltaT)*self.deltaT
        
        return self.pm.particleList
            






    
    

