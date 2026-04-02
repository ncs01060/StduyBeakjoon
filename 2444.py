n = int(input())
cnt = -1
for i in range(1,n+1):
    cnt += 2
    print(" " * (n - i) + "*" * cnt)

cnt -= 2
for i in range(n-1,0,-1):
    print(" " * (n - i) + "*" * cnt)
    cnt -= 2