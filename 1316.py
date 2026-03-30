n = int(input())
count = 0
for i in range(n):
    sw = True
    already = []
    word = input()
    for j in range(len(word)):
        if word[j] not in already:
            already.append(word[j])
        elif word[j-1] == word[j]:
            continue
        else:
            sw = False
    if sw:
        count+=1
print(count)

