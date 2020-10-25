rounds , hands = input().split()
rounds = int(rounds)
hands = int(hands)

cards = input()
move = input()

during = []
pre = []
weigh = {'2':1,'3':1,'4':1,'5':1,'6':1,'7':1 ,'8':1,'9':1,'X':1,'J':1,'Q':1,'K':1,'A':1}
list = ['2','3','4','5','6','7','8','9','X','J','Q','K','A']

def judge():
    for i in range(rounds):
        if move[i] == 'n':
            if cards[i] in during:
                print("impossible")
                return 0
            during.append(cards[i])
            weigh.pop(cards[i])
        
        if move[i] == 'y' and cards[i] not in during:
            pre.append(cards[i])
            weigh[cards[i]]+=1

    if len(pre) > hands:
        print("impossible")
        return 0
    return pre

result = judge()
if result:
    d_order=sorted(weigh.items(),key=lambda x:x[1],reverse=True)
    num = hands - len(result)
    dnf = 0
    for i in range(num):
        while weigh[d_order[dnf][0]] ==4:
            dnf+=1
        result.append(d_order[dnf][0])
        weigh[d_order[dnf][0]] +=1

    if result:
        find = []
        for each in result:
            find.append(list.index(each))
        find = sorted(find)
        for each in find:
            print(list[each],end='')