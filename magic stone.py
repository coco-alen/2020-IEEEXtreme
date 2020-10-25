import sys
sys.setrecursionlimit(100000)

T = int(input())

for i in range(T):
    W = set()
    B = set()
    N = int(input())
    WC = [0]*(N+1)
    BC = [0]*(N+1)
    WC[1:N+1] = list(map(int,input().split()))
    BC[1:N+1] = list(map(int,input().split()))
    for item in WC[1:]:W.add(item)
    for item in BC[1:]:B.add(item)
    if len(W) == N and len(B) == N:
        print('impossible')
        continue

    ostate = set()
    for i in range(1,N+1):
        ostate.add(i)

    VisState = set()
    Op = [-1]*100000

    def judge(state,pos):
        #print(state,pos)
        if len(state) == 1:
            Op[pos] = -1
            return True
        #str_state = ''.join(map(str,state))
        str_state = ''.join(str(state))
        if str_state in VisState:return False
        VisState.add(str_state)

        Nstate = set()
        Op[pos] = 'W'
        for item in state:
            Nstate.add(WC[item])
        if judge(Nstate,pos+1):return True

        Nstate=set()
        Op[pos] = 'B'
        for item in state:
            Nstate.add(BC[item])
        if judge(Nstate, pos + 1): return True

        return False
    if not judge(ostate,0):
        print('impossible')
    else:
        temp = 0
        while Op[temp]!=-1:
            print(Op[temp],end = '')
            temp += 1
        print()

