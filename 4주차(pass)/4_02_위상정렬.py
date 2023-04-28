# 1번을 해보세요!
def topological_sort(graph):
    #정점(key)의 진입차수(value) Set
    inDeg = {}
    #초기화
    for v in graph : 
        inDeg[v] = 0
    #간선 세기
    for v in graph : 
        for u in graph[v] : 
            #진입차수 이므로 들어오는 정점에서 세어야함
            inDeg[u] += 1
    
    #진입차수 0 정점 리스트 vlist
    vlist = []
    for v in graph : 
        if inDeg[v] == 0 : 
            vlist.append(v)

    #vlist에서 하나 뽑기

    #다시 간선 업데이트 -> vlist에 넣기 -> ... -> vlist 빌 때 까지
    while vlist :
        vpop = vlist.pop()
        print(vpop, end=" ")
        #간선 업데이트, 뺀거로부터 오는 정점 빼기
        for u in graph[vpop] : 
            inDeg[u] -= 1
            if inDeg[u] == 0 : 
                vlist.append(u)


# 2번을 해보세요!
mygraph = dict()
#정점의 개수 v
vnum = int(input())
#정점의 개수 만큼 key 생성, value 공집합(초기화)
for i in range(vnum) :
    mygraph[chr(65+i)] = set()

#간선의 개수 unum
unum = int(input())

#간선으로 연결된 두 정점
for _ in range(unum) : 
    p1, p2 = input().split()[:2]
    mygraph[p1] |= {p2}

# 출력합니다!
print('topological_sort: ')
topological_sort(mygraph)
print()