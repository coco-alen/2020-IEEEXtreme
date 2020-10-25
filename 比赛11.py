shelter = int(input())
soldier = list(map(int,input().split()))
day = int(input())
weather = []
for i in range(day):
    weather.append(list(map(int,input().split())))

sum = 0
for each in weather:
    sum +=each[-1]
print(weather)
print(sum)
