import numpy as np

def task1_1(position):
    return position[0]**2 + position[1]**2 + 1

def task1_3(n_particles, particle_position_vector):
    velocity_vector = ([np.array([0, 0]) for _ in range(n_particles)])
    iteration = 0
    while iteration < n_iterations:
        for i in range(n_particles):
            fitness_cadidate = task1_1(particle_position_vector[i])
            print(fitness_cadidate, ' ', particle_position_vector[i])
            
            if(pbest_fitness_value[i] > fitness_cadidate):
                pbest_fitness_value[i] = fitness_cadidate
                pbest_position[i] = particle_position_vector[i]

            if(gbest_fitness_value > fitness_cadidate):
                gbest_fitness_value = fitness_cadidates
                gbest_position = particle_position_vector[i]

        if(abs(gbest_fitness_value - target) < target_error):
            break
        
        for i in range(n_particles):
            new_velocity = (W*velocity_vector[i]) + (c1*random.random()) * (pbest_position[i] - particle_position_vector[i]) + (c2*random.random()) * (gbest_position-particle_position_vector[i])
            new_position = new_velocity + particle_position_vector[i]
            particle_position_vector[i] = new_position

        iteration = iteration + 1

def task1_5():
    """
    The choice of population size is related to the complexity of the problem. As the complexity of the problem
    increases, the population size also grows
    The inertia weight ω affects the particle’s global and local search ability.
    Along with the increase of the maximum velocity, mean fitness value is decreasing and success rate is increasing, which means
    the convergence and stability of the algorithm is becoming stronger and stronger. 
    """

def task2_1(parents, n_offspring):
    n_parents = len(parents)
    
    offspring = []
    for i in range(n_offspring):
        random_dad = parents[np.random.randit(low - 0, high = n_parents - 1)]
        random_mom = parents[np.random.randit(low - 0, high = n_parents - 1)]
        mask_dad = np.random.randit(0, 2, size = np.array(random_dad).shape)
        mask_mom = np.logical_not(mask_dad)
        child = np.add(np.multiply(random_dad, mask_dad), np.multiply(random_mom, mask_mom))
        offspring.append(child)

def task2_3():
    """
    population size says how many chromosomes are in population
    crossover probabibility says how often crossover will be performed
    mutation probabibility says how often mutation will occur
    """
