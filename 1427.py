# num = input()
# sorted_num = []
# for i in num:
#     sorted_num.append(i)
#
# sorted_num.sort(reverse=True)
# for i in sorted_num:
#     print(i,end="")

# print(''.join(sorted(input(),reverse=True)))

num = input()
num = sorted(num,reverse=True)
print(''.join(num))