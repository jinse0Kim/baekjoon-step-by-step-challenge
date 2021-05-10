T = int(input())
for x in range(T):
    R,S = input().split()
    result = ""
    for x in S:
        result += int(R)*x
    print(result)