W,H,A,B,M,C = map(int,input().split())

if W % A ==0:
    wieth = W//A 
    cut_heigh = 0
else:
    wieth =  W//A+1
    cut_heigh = H

if H % B ==0:
    heigh = H//B
    cut_line = 0
else:
    heigh = H//B+1
    cut_line = W

if wieth*heigh % 10 ==0:
    num = wieth*heigh//10
else:
    num = wieth*heigh//10 + 1

cost = num*M + (cut_heigh+cut_line)*C
print(cost)