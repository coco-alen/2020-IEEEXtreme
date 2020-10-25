num_begin = int(input())
hash_ = input()
hash = [int(j) for j in hash_.split()]
Q = int(input())
K =[]
output = dict()

for i in range(Q):
    K.append(input())

for each in K:
    output[each] = -1 

left = [1,2,3,4,5]
count =0
track = [[1,2,3,4,5]]

while(1):
    length = len(left)
    if str(length) in K:
        if output[str(length)] ==-1:
            output[str(length)] = count
    left2 = []
    for each in left:
        left2.append(hash[each-1])
    left = left2.copy()
    left = list(set(left))
    if left in track:
        break
    count+=1
    track.append(left)
for each in K:
    print(output[each])