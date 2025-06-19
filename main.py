from main.Renderer import App
from main.Particle import Particle, ParticleManager
from main.Solver import Solver
from main.Vector2D import Vector2D
import threading
import time




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

def simulation_loop(solver, lock, stop_event, sim_dt=0.001):
    while not stop_event.is_set():
        with lock:
            solver.step()
        time.sleep(sim_dt)

if __name__=="__main__":
    dam_height = 25
    spacing = 5.0
    domain_width = 50
    domain_height = dam_height
    window_width = 3*domain_width * spacing
    window_height = 3 * dam_height * spacing
    particles = init_sph_dam_break(domain_width, domain_height, spacing=spacing, fill_ratio=1.0)
    solver = Solver(H=spacing*3, rho0=1.0, k=1.0, domain_width=window_width, domain_height=window_height)
    solver.set_particles(particles)
    particle_lock = threading.Lock()
    stop_event = threading.Event()
    sim_thread = threading.Thread(target=simulation_loop, args=(solver, particle_lock, stop_event))
    sim_thread.start()
    try:
        app = App(particles, solver, particle_lock, window_width=window_width, window_height=window_height)
    finally:
        stop_event.set()
        sim_thread.join()



