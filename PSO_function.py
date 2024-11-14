import random
import math

def f1(x):
    return (x - 1)**2 * (x - 8)**2

def f2(x):
    return 4 * 39 * (x - 10)**2 + 4

def f3(x1, x2):
    return x1**2 * math.cos(2 * x1) + x2**2 * math.cos(2 * x2) + 2

def pso_algorithm_1d(func, n_iterations=100, intervalle=(3, 10), n_particules=3):
    particles = [random.uniform(*intervalle) for _ in range(n_particules)]
    velocities = [0.0 for _ in range(n_particules)]
    best_particles = particles[:]
    best_global = min(best_particles, key=func)
    
    w = 0.5      
    Pg0 = best_global
    
    for _ in range(n_iterations):
        b1, b2 = random.random(), random.random()
        
        for i in range(n_particules):
            velocities[i] = (w * velocities[i] +
                               b1 * (best_particles[i] - particles[i]) +
                               b2 * (best_global - particles[i]))
            
            particles[i] += velocities[i]
            
            if func(particles[i]) < func(best_particles[i]):
                best_particles[i] = particles[i]
        
        best_global = min(best_particles, key=func)
        
        if func(best_global) >= func(Pg0):
            break
        
        Pg0 = best_global
    
    return best_global, func(best_global)

def pso_algorithm_2d(n_iterations=100, intervalle_x1=(3, 10), intervalle_x2=(3, 10), n_particules=3):
    particles = [(random.uniform(*intervalle_x1), random.uniform(*intervalle_x2)) for _ in range(n_particules)]
    velocities = [(0.0, 0.0) for _ in range(n_particules)]
    best_particles = particles[:]
    best_global = min(best_particles, key=lambda p: f3(p[0], p[1]))
    
    w = 0.5      
    Pg0 = best_global
    
    for _ in range(n_iterations):
        
        b1, b2 = random.random(), random.random()
        
        for i in range(n_particules):
            velocities[i] = (w * velocities[i][0] +
                            b1 * (best_particles[i][0] - particles[i][0]) +
                            b2 * (best_global[0] - particles[i][0]),
                            w * velocities[i][1] +
                            b1 * (best_particles[i][1] - particles[i][1]) +
                            b2 * (best_global[1] - particles[i][1]))
            
            particles[i] = (particles[i][0] + velocities[i][0],
                            particles[i][1] + velocities[i][1])
            
            if f3(particles[i][0], particles[i][1]) < f3(best_particles[i][0], best_particles[i][1]):
                best_particles[i] = particles[i]
        
        best_global = min(best_particles, key=lambda p: f3(p[0], p[1]))
        
        if f3(best_global[0], best_global[1]) >= f3(Pg0[0], Pg0[1]):
            break
        
        Pg0 = best_global
    
    return best_global, f3(best_global[0], best_global[1])

solution_f1, valeur_minimale_f1 = pso_algorithm_1d(f1)
print("La solution optimale pour f1(x) est x =", solution_f1)
print("La valeur minimale de f1(x) est f1(x) =", valeur_minimale_f1)

solution_f2, valeur_minimale_f2 = pso_algorithm_1d(f2)
print("La solution optimale pour f2(x) est x =", solution_f2)
print("La valeur minimale de f2(x) est f2(x) =", valeur_minimale_f2)

solution_f3, valeur_minimale_f3 = pso_algorithm_2d()
print("La solution optimale pour f3(x1, x2) est (x1, x2) =", solution_f3)
print("La valeur minimale de f3(x1, x2) est f3(x1, x2) =", valeur_minimale_f3)
