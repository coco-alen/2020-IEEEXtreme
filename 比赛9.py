n = int(input())
connect = []
for i in range(n):
    connect.append(int(input()))

location = []
def distance(x1,y1,x2,y2):
    return (x1-x2)**2+(y1-y2)**2

def dis(x,y,location):
    sum = 0
    for each in location:
        sum = sum+distance(x,y,each[0],each[1])


def find(n):
    location = []
    if n == 1:
        location.append([10,10])
    else:
        location = find(n-1)
        frend_x= location[connect[n-2]][0]
        frend_y= location[connect[n-2]][1]
        possible = [[frend_x+1,frend_y],[frend_x-1,frend_y],[frend_x,frend_y+1],[frend_x,frend_y-1]]
        min = 10000
        for each in possible:
            if each not in location:
                if dis(each[0],each[1],location) < min:
                    location.append([each[0],each[1]])
        return location
        
location = find(n)
result = 0
for each in location:
    result +=dis(each[0],each[1],location)
print(result)

