#1916619백주연

# 1번을 해보세요!
def distance(p1,p2) :
    return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5

def closest_pair(p):
    n = len(p)
    mindist = float("inf")
    #가능한 모든 쌍
    #점 하나 선택(i = 0~n-2), 그 뒤로 점들(i+1~n-1)과의 거리
    for i in range(n-1) : 
        for j in range(i+1, n) :
            #거리 계산
            dist = distance(p[i], p[j])
            #거리 비교
            if dist < mindist :
                mindist = dist
    
    return mindist

# 2번을 해보세요!
#점의 쌍 개수
n = int(input())
#한 튜플 내 들어가는 두개의 숫자가 공백으로 구분되어 주어짐
p = [(int(x), int(y)) for x, y in [input().split()[:2] for _ in range(n)]]

# 출력합니다!
print("최근접 거리:", closest_pair(p))