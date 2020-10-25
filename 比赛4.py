
def ror(words):
    length = len(words)
    return words[length - 1:] + words[:length - 1]

light_num, all = input().split()
light_num = int(light_num)
all = int(all)

light =[]
light_num = input()
light = [int(j) for j in light_num.split()]

b_light = ''
for i in range(all):
    if i in light:
        b_light = b_light + '1'
    else:
        b_light = b_light + '0'

count = 0
b_light_org = b_light
while ror(b_light) != b_light_org:
    b_light = ror(b_light)
    count +=1
print(count)