def judge(a,b):
    temp = 1
    for i in range(len(a)):
        if a[i] !=b[i]:
            if temp:
                temp = 0
            else:
                return 0
    return 1

n = int(input())

codes = []
for i in range(n):
    codes.append(input())

count = 0
for i in range(n):
    for j in range(i+1,n):
        if judge(codes[i],codes[j]):
            count+=1
print(count)