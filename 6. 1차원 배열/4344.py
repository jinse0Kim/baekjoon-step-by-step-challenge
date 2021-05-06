T = int(input())
for x in range(T):
    test_list = list(map(int,input().split()))
    test_avg = sum(test_list[1:])/test_list[0]
    avg_student = 0
    for score in test_list[1:]:
        if score > test_avg:
            avg_student += 1
    rate = avg_student/test_list[0] * 100
    print(f'{rate:.3f}%')