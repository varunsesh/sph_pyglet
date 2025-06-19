from main.Vector2D import Vector2D


class Particle:
    
    def __init__(self, x, y, rho=1.0):
        self.position = Vector2D(x, y)
        self.velocity = Vector2D(0.0, 0.0)
        self.radius = 1.0
        self.rho = rho

    def update(self, dx, dy):
        self.position += Vector2D(dx, dy)
        


class ParticleManager():
    
    def __init__(self):
        self.particleList = []

    def addParticle(self, x, y, rho):
        particle = Particle(x,y,rho)
        
        self.particleList.append(particle)
        return len(self.particleList)-1

    



if __name__=="__main__":
    p1 = Particle(20,30)
    print(f"{p1.position}")



