from main.Vector2D import Vector2D


class Particle:
    
    def __init__(self, x, y, rho):
        self.position = Vector2D(x, y)
        self.velocity = Vector2D(0.0, 0.0)
        self.rho = rho
        


class ParticleManager():
    
    def __init__(self):
        self.particleList = []

    def addParticle(self, x, y, rho):
        particle = Particle(x,y,rho)
        
        self.particleList.append(particle)
        return len(self.particleList)-1

    






