
def findAllPath(graph,start,end):
    path=[]
    stack=[]
    stack.append(start)
    visited=set()
    visited.add(start)
    seen_path={}
    #seen_node=[]
    while (len(stack)>0):
        start=stack[-1]
        nodes=graph[start]
        if start not in seen_path.keys():
            seen_path[start]=[]     
        g=0
        for w in nodes:
            if w not in visited and w not in seen_path[start]:
                g=g+1
                stack.append(w)
                visited.add(w)
                seen_path[start].append(w)
                if w==end:
                    path.append(list(stack))
                    old_pop=stack.pop()
                    visited.remove(old_pop)
                break    
        if g==0:
            old_pop=stack.pop()
            del seen_path[old_pop]
            visited.remove(old_pop)
    return path
    
goal = []
people_num, connect_list = input().split()
people_num = int(people_num)
connect_list = int(connect_list)
connect = dict()
for i in range(people_num):
    connect[i+1] = []
for i in range(connect_list):
    people1 , people2 = input().split()
    people2 = int(people2)
    people1 = int(people1)
    connect[people1].append(people2)
    connect[people2].append(people1)
goal_num = int(input())
for i in range(goal_num):
    source, end = input().split()
    goal.append([source,end])


for each in goal:
    start = int(each[0])
    stop = int(each[1])
    path = findAllPath(connect,start,stop)
    
    ans = set(path[0]).intersection(*path[1:])
    print(len(ans))



