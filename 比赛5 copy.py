from collections import Counter
n=int(input())
nums=list(map(int,input().strip().split()))
dic=Counter()

for i in nums:   #计算每个数字有多少个
    dic[i]+=1
count=Counter()
count[len(dic)]=1 #计算遗留数据长度
dfn=2

while True:
    dic1=Counter()
    for i in dic:
        dic1[nums[i-1]]+=1
    dic=dic1
    if len(dic) in count:
        break
    count[len(dic)]=dfn
    dfn+=1


q=int(input())
for i in range(q):
    t=int(input())
    if t in count:
        print(count[t])
    else:
        print(-1)
