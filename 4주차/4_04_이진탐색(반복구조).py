#1916619백주여
# 1번을 해보세요!
def binary_search_iter(A, key, low, high) :
    while(low <= high) :
        mid = (low + high)//2
        if (A[mid] < key) : low = mid+1
        elif (A[mid] > key) : high = mid -1
        else :
            return mid
    return -1


# 2번을 해보세요!
listA = [int(n) for n in input().split()]
key = int(input())

# 출력합니다!
print("입력 리스트 =", listA)
print("%d 탐색(반복) -->" %(key), binary_search_iter(listA, key, 0, len(listA)-1) )