from main.Vector2D import Vector2D
from main.Particle import Particle, ParticleManager
import math


class Solver():
    

    def __init__(self, H, rho0, k):
        self.pm = ParticleManager()
        self.deltaT = 0.01
        self.H = H
        self.rho0 = rho0
        self.k = k #constant for pressure density equivalence (compressiblity thingy perhaps)
        self.HSQ = self.H*self.H
        self.__kernel_constant = 315/(1*math.pi*pow(H, 9.0))



    # def init_sph(self, Re, height):
    #     number_particles = 16
        
    #     for y in range(0,height):
    #         for x in range(0,height):
    #             self.pm.addParticle(x,y,1.0)

    #     return self.pm.particleList

    def set_particles(self, particle_list):
        self.pm.particleList = particle_list

    def step(self):
        self.compute_density_pressure()
        self.compute_forces()
        self.update_pos()

    ## Using Poly6 Kernel Function
    def compute_density_pressure(self):
        r = Vector2D(0.0, 0.0)
        for pi in self.pm.particleList:
            pi.rho = 0.0
            for pj in self.pm.particleList:
                r2 = (pj.position.distance_to(pi.position))**2
                if (r2<self.HSQ):
                    pi.rho += 1*self.__kernel_constant*(self.HSQ-r2)**3
            pi.p = self.k*pi.rho - self.rho0


    def compute_forces(self):
        # Basic SPH: pressure, viscosity, and gravity
        g = Vector2D(0.0, -9.81)  # gravity
        for pi in self.pm.particleList:
            f_pressure = Vector2D(0.0, 0.0)
            f_viscosity = Vector2D(0.0, 0.0)
            for pj in self.pm.particleList:
                if pi is pj:
                    continue
                r_vec = pj.position - pi.position
                r = r_vec.length()
                if r < self.H and r > 0:
                    # Pressure force (simplified)
                    f_pressure += -r_vec.normalized() * (pi.p + pj.p) / (2 * pj.rho)
                    # Viscosity force (simplified)
                    f_viscosity += (pj.velocity - pi.velocity) / pj.rho
            # Add gravity
            pi.force = f_pressure + f_viscosity + g

    def update_pos(self):
        for p in self.pm.particleList:
            # Simple explicit Euler integration
            acc = p.force / p.rho if hasattr(p, 'force') and p.rho != 0 else Vector2D(0, 0)
            p.velocity += acc * self.deltaT
            p.position += p.velocity * self.deltaT
        return self.pm.particleList










