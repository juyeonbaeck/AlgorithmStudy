# 1번을 해보세요!
def insertion_sort(A) :
    n = len(A)
    #i = 1 ~ n-2
    for i in range(1, n) :
        key = A[i]
        j = i-1
        #key보다 작거나 같은 값이 나올 때 까지 한칸씩 미룸
        while j>=0 and A[j] > key :
            A[j+1] = A[j]
            j = j-1
        #넣을 자리 찾으면
        A[j+1] = key
        printStep(A, i)

# 중간 과정을 출력하는 함수에요!
def printStep(arr, val) :
    print("  Step %2d = " % val, end='')
    print(arr)

# 2번을 해보세요!
data = [int(n) for n in input().split()]

# 출력합니다!
print("Original  :", data)
insertion_sort(data)
print("Insertion :", data)