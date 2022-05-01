class Graph:
    def __init__(self,adjacentList):
        self.adjacentList=adjacentList

    def dfid(self,start,goal,maxlimit):
        print('\n---- DFID ----')
        for limit in range(maxlimit+1):
            print('\nIteration with depth limit ',limit,' : ')
            path = []
            if self.DLS(start, goal, limit, path):
                return True
        return False

    def DLS(self,node,goal,limit, path):
        path.append(node)
        if node == goal:
            print(path)
            return True
       
        if limit <= 0:
            print(path)
            return False
   
        for neighbour in self.adjacentList[node]:
            if self.DLS(neighbour,goal,limit-1,path):
                return True
        
        
        return False
nodes = [ item for item in input('Enter nodes :').split(' ')]
start = input("Enter the start Node") 
goal = input("Enter the goal Node")
adj={}
for vertex in nodes:    
    values = input('enter edges from {} :'.format(vertex))
    lst=values.split(",")
    print(lst)
    if(lst==['']):
        lst.clear()

    adj[vertex]=lst
    
print(adj)
path=[]


maxlimit = int(input("Enter max depth : "))
graph1 = Graph(adj)


if graph1.dfid(start, goal, maxlimit):
    print("\nThe goal node was found !!")
else:
    print("\nThe goal node was NOT found !!")