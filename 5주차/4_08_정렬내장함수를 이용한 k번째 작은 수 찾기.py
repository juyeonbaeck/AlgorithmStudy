# 1번을 해보세요!
def kth_smallest_sort(A, k): 
    #리스트 정렬 - 내장함수 sort ;리스트 오름차순 정렬
    A.sort()
    #k번째 반환
    return A[k-1]

# 2번을 해보세요!
array = [int(n) for n in input().split()]
k = int(input())


# 출력합니다!
print("입력 리스트 =", array) 
print("[정렬기법] %d번째 작은 수: " %(k), kth_smallest_sort(array, k)) 