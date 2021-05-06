n = int(input())  
test_list = list(map(int, input().split()))
max_score = max(test_list)

new_list = []
for x in test_list :
    new_list.append(x / max_score * 100) 
test_avg = sum(new_list)/n
print(test_avg)