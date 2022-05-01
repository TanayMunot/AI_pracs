nodes = [ item for item in input('Enter nodes :').split(' ')]
startnode = input("enter start node")
goalnode = input("Enter the goal Node")
maxd = input("Enter deptth limit")
level=0 
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

def dls(startnode,goalnode,level,maxd,path):
    print("Current Node : {}".format(startnode))
    path.append(startnode)
    if startnode == goalnode:
        print("Goal Node Found")
        return path
    if level == maxd:
        return False   
    for neighbours in adj[startnode]:
        if dls(neighbours,goalnode,level+1,maxd,path):
            return path

    path.pop()

    return False

# Driver Code
result = dls(startnode,goalnode,level,maxd,path)
if(result):
    print("Path Found : {}".format(result))
else:
    print("Path does not exist in the given limit")

