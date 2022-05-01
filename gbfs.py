class Graph:
    def __init__(self,adjacentList):
        self.adjacentList=adjacentList
    
    def get_neighbours(self, node):
        return self.adjacentList[node]
        
    def heuristic(self,n):
        H ={
            'A':12,
            'B':4,
            'C':7,
            'D':3,
            'E':8,
            'F':2,
            'H':4,
            'I':9,
            'S':13,
            'G':0
            
        }
        return H[n]
        
    def a_star_algorithm(self,start,goal):
        
        open_lst = set([start])
        closed_lst = set([])
        
        
 
        # par contains an adjac mapping of all nodes
        par = {}
        par[start] = start
        
        while len(open_lst) > 0:
            n = None
 
            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or self.heuristic(v) < self.heuristic(n):
                    n = v
 
            if n == None:
                print('Path does not exist!')
                return None
                
            # if the current node is the stop
            # then we start again from start
            if n == goal:
                path = []
 
                while par[n] != n:
                    path.append(n)
                    n = par[n]
 
                path.append(start)
 
                path.reverse()
 
                print('Path found: {}'.format(path))
                return path
                
               
            for (m, weight) in self.get_neighbours(n):
              
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
 
            
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return None
        
nodes = [ item for item in input('Enter nodes :').split(' ')]
startnode = input("Enter the start Node") 
goal = input("enter goal node")
adj={}
for vertex in nodes:
    
    values = int(input('enter no of edges from {}'.format(vertex)))
    lst=[]
    for values in range(0,values):
        v = input("Input Node and weight comma seprated : ")
        l = v.split(",")
        l[1]=int(l[1])
        t = tuple(l)
        lst.append(t)
    print(lst)
    adj[vertex]=lst
    
r=[]
for key, value in adj.items():
     if not value:
            r.append(key)

for k in r:
    adj.pop(k)
            
print(adj)
    
print(nodes)

#adjacentList = {'A': [('B', 3), ('C', 4), ],'B': [('A',3),('D', 4),('C',5)],'C': [('B',5),('E', 2)],'D':[('B',4),('E',5),('F',4)],'E':[('C',2),('D',5),('G',4)],'F':[('D',4)],'G':[('E',4),('H',3)],'H':[('G',3)]}
graph1 = Graph(adj)
graph1.a_star_algorithm(startnode,goal)
