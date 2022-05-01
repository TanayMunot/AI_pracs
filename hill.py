import random

def init_solution(tsp):
    cities = list(range(len(tsp))) # possible cities - 0,1,...n
    solution = []

    for i in range(len(tsp)):
        city = cities[random.randint(0, len(cities) - 1)]
        solution.append(city)
        cities.remove(city) # each city has to be chosen only once

    return solution

def get_length(tsp, solution):
    length = 0
    for i in range(len(solution)):
        length += tsp[solution[i - 1]][solution[i]]
    return length

def get_neighbours(solution):
    neighbours = []
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            neighbour = solution.copy()
            neighbour[i] = solution[j]
            neighbour[j] = solution[i]
            neighbours.append(neighbour)
    return neighbours

def get_best(tsp, neighbours):
    bestlen = get_length(tsp, neighbours[0])
    bestnei = neighbours[0]
    for neighbour in neighbours:
        curlen = get_length(tsp, neighbour)
        if curlen < bestlen:
            bestlen = curlen
            bestnei = neighbour
    return bestnei, bestlen

def hillclimb(tsp):
    cursolution = init_solution(tsp)
    curlen = get_length(tsp, cursolution)
    neighbours = get_neighbours(cursolution)
    bestneighbour, bestlen = get_best(tsp, neighbours)

    while bestlen < curlen:
       print()
       print("Current Solution : ",cursolution)
       print("Current Length : ",curlen)
       print()
       cursolution = bestneighbour
       curlen = bestlen
       neighbours = get_neighbours(cursolution)
       bestneighbour, bestlen = get_best(tsp, neighbours)
    
    print("Best Solution : ",cursolution)
    print("Best Length : ",curlen)
    print()
    


n = int(input("Enter number of cities : "))
tsp = []

for i in range(n):
    dist = []
    for j in range(n):
        if i==j:
            dist.append(0)
        elif j>i:
            dist.append(int(input("Enter dist between city "+str(i+1)+" and city "+str(j+1)+" :")))
        else:
            dist.append(tsp[j][i])
    tsp.append(dist)
        
            
        
hillclimb(tsp)