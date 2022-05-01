import random

def mutate(chromosome,prob):
    chromosome = [char for char in chromosome]
    #print(chromosome)
    for i in range(len(chromosome)):
        if random.random()<prob:
            if chromosome[i] == '1':
                chromosome[i] = '0'
            else:
                chromosome[i] = '1'
    
    new_chromo = ""
    return new_chromo.join(chromosome)
    
n = int(input("Enter population size"))
prob = float(input("Enter mutation probability : "))
for i in range(n):  
    chromosome = input("Enter chromosome : ")
    new_chromosome = mutate(chromosome,prob)
    print("\nMutated Chromosome : ",new_chromosome)
    




