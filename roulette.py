import numpy as np

def get_fitness(chromosome):
    fitness = 0
    for char in chromosome:
        if char=='1':
            fitness += 1
    
    return fitness
    
def roullete_wheel(population,fitness):
    pop_fitness = sum(fitness)
    probabilities = [fit/pop_fitness for fit in fitness]
    print()
    for i,prob in enumerate(probabilities):
        print('Selection probability for chromosome ',i,' = ',prob)
    
    print("\nSpinning wheel...")
    print("Chromosome selected : ",
    np.random.choice(population,p=probabilities))
    

n = int(input("Enter number of individuals in population : "))
population = []
fitness = []
for ind in range(n):
    chromosome = input("Enter chromosome "+str(ind) + " : ")
    population.append(chromosome)
    fitness.append(get_fitness(chromosome))
    
roullete_wheel(population,fitness)