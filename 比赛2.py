list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

L = [[] for i in range(4)]
for i in range (4):
    for j in range(4):
        L[i].append(list[1])
L[1][0]=L[1][1]=L[2][0]=L[3][0]=list[2]
L[1][2]=L[1][3]=L[2][3]=L[3][3]=list[3]
L[2][1]=L[3][1]=L[2][2]=L[3][2]=list[4]

def creat(n):
    if n ==4:
        return L
    else:
        result = creat(n-1)
        for i in range(n-3):
            result[i].append(result[i][n-2])

        result.append([])
        for i in range(n-3):
            result[n-1].append(result[n-2][i])
        for i in range(3):
            result[n-1].append(list[n])
        for i in range(2):
            result[n-2-i].append(list[n])
        return result
n=[]
T =int(input())
for i in range(T):
    n.append(int(input()))

for nums in n:
    if nums == 1:
        print('a')
    elif nums ==2:
        print('ab\naa')
    elif nums ==3:
        print('impossible')
    else:
        answer = creat(nums)
        for each in answer:
            for word in each:
                print(word,end='')
            print('')
        for i in range(n):
            list.pop()