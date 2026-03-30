l = [0] * 30
for i in range(28):
    s = int(input())
    l[s-1] = 1

for j in range(0,len(l)):
    if l[j] == 0:
        print(j+1)