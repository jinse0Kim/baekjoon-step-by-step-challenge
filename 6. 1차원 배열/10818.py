num = int(input())
num_list = list(map(int,input().split()))
max_num = num_list[0]
min_num = num_list[0]

for x in num_list:
    if x > max_num:
        max_num = x
    if x < min_num:
        min_num = x
print(min_num,max_num)
    