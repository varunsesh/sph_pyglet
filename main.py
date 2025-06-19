from main.Renderer import App
from main.Particle import Particle, ParticleManager
from main.Solver import Solver
from main.Vector2D import Vector2D




def init_sph(Re, height, spacing=1):
    pm = ParticleManager()
    dx = Vector2D(20.0, 0.0)
    dy = Vector2D(0.0, 20.0)
    
    for y in range(0,height):
        for x in range(0,height):
            pm.addParticle(x*spacing,y*spacing,1.0)
    return pm.particleList

def init_sph_dam_break(domain_width, domain_height, spacing=20.0, fill_ratio=0.4):
    pm = ParticleManager()
    fill_width = int(domain_width * fill_ratio)
    fill_height = int(domain_height * fill_ratio)
    for y in range(fill_height):
        for x in range(fill_width):
            pm.addParticle(x * spacing, y * spacing, 1.0)
    return pm.particleList



if __name__=="__main__":
    dam_height = 25
    spacing = 5.0
    domain_width = 50
    domain_height = dam_height
    window_width = 3*domain_width * spacing
    window_height = 3 * dam_height * spacing
    particles = init_sph_dam_break(domain_width, domain_height, spacing=spacing, fill_ratio=1.0)
    solver = Solver(H=spacing*3, rho0=1.0, k=1.0)  # Example kernel radius, adjust as needed
    solver.set_particles(particles)
    app = App(particles, solver, window_width=window_width, window_height=window_height)



