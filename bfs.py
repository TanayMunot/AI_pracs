nodes = [ item for item in input('Enter nodes :').split(' ')]
startnode = input("Enter the start Node") 
goal = input("enter goal node")
adj={}
for vertex in nodes:    
    values = input('enter  edges from {} :'.format(vertex))
    lst=values.split(",")
    print(lst)
    if(lst==['']):
        lst.clear()

    adj[vertex]=lst
    
print(adj)
    
visit = [] # List to keep track of visited nodes.
q = []     #Initialize a queue

def bfs(visit, adj, node,goal):
    visit.append(node)
    q.append(node)
    while len(q)!=0:
        s = q.pop(0)
        if s == goal:
          return True
        for neighbour in adj[s]:
          if neighbour not in visit:
               visit.append(neighbour)
               q.append(neighbour)
    return False 
    
# Driver Code
res = bfs(visit, adj, startnode,goal)
if res :
    print("Goal Node found")
    print("Path : {}".format(visit))
else :
    print("Goal Not found")

