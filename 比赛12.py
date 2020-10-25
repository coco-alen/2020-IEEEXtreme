
goal,M = input().split()
goal = int(goal)
M = int(M)
sale = []
set1 = [0,0,0]
set2 = [0,0,0]
set3 = [0,0,0]

for i in range(M):
    temp = input()
    temp = temp.split(' ')
    sale.append(temp)

print(sale)

for each in sale:
    if each[0] == 'Zulian':
        set1[0] +=int(each[1])
    elif each[0] == 'Razzashi':
        set1[1] +=int(each[1])
    elif each[0] == 'Hakkari':
        set1[2] +=int(each[1])
    elif each[0] == 'Sandfury':
        set2[0] +=int(each[1])
    elif each[0] == 'Skullsplitter':
        set2[1] +=int(each[1])
    elif each[0] == 'Bloodscalp':
        set2[2] +=int(each[1])
    elif each[0] == 'Gurubashi':
        set3[0] +=int(each[1])
    elif each[0] == 'Vilebranch':
        set3[1] +=int(each[1])
    elif each[0] == 'Witherbark':
        set3[2] +=int(each[1])
    
result = min(set1) + min(set2) + min(set3)
print(result)