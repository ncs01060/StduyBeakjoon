receipt = int(input())
something_len = int(input())
total = 0
for i in range(something_len):
    money, count = map(int,input().split())
    total += money * count

if total == receipt:
    print("Yes")
else:
    print("No")