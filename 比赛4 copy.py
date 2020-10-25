N,T=map(int,input().split())
light_num = input()
s= [int(j) for j in light_num.split()]
s.sort()
def dfs(s):
    for i in range(1,n):
        diff=s[i]-s[0]
        flag=0
        for j in range(n):
            if (s[j]+diff)%t!=s[(i+j)%n]:
                flag=1
                break
        if flag==0:return diff-1
    return t-1
print(dfs(s))