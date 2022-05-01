nodes = [ item for item in input('Enter nodes :').split(' ')]
startnode = input("Enter the start Node") 
goalnode = input("Enter the goal Node")
adj={}
for vertex in nodes:    
    values = input('enter edges from {} :'.format(vertex))
    lst=values.split(",")
    print(lst)
    if(lst==['']):
        lst.clear()

    adj[vertex]=lst
    
print(adj)
    
visited = set() # Set to keep track of visited nodes.
path = []
def dfs(visited, graph, node,goal):
    path.append(node)
    if node == goal:
        return path

    if node not in visited:
        
        visited.add(node)
        for neighbour in graph[node]:
           if dfs(visited, graph, neighbour,goal):
               return path

    path.pop()

    return False
    

# Driver Code
res = dfs(visited, adj, startnode,goalnode)
if res :
    print("Goal Node Found !")
    print("Path : {}".format(res))
else:
    print("Goal Node Not found")