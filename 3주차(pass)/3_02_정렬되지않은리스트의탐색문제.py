# 1번을 해보세요!
def sequential_search(A, key):
    for i in range(len(A)) :
        if key == A[i] :
            return i
    return -1

# 2번을 해보세요!
A = [int(n) for n in input().split() ]
# 3번을 해보세요!
key = int(input())

# 출력합니다!
print(sequential_search(A, key))