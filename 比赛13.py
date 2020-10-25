def mysum(starti,startj,heigh,weigh,mat):
    result = 0
    for i in range(heigh):
        result = result + sum(mat[i+starti][startj:startj+weigh-1])

N,M,R,C = input().split()
N = int(N)
M = int(M)
R = int(R)
C = int(C)

color = []
for i in range(R):
    temp = input()
    temp = temp.split(' ')
    color.append(temp)


heigh = N//R 
more_heigh = N % R

weigh = M//C
more_weigh = M % C

scan_heigh = R - more_heigh
scan_weigh = C - more_weigh

print(mysum(0,0,2,3,color))