# 1번을 해보세요!
def dfs(graph, start, visited ):
    if (start not in visited) : 
        visited |= {start}
        print(start, end=" ")
        nextstart = graph[start] - visited
        for v in nextstart :
            dfs(graph, v, visited)

# 2번을 해보세요!
mygraph = dict()
#간선의 개수 n
n = int(input())
#n쌍 만큼 두 정점 리스트
for i in range(n) : 
    # 두 점을 입력받음
    e1, e2 = input().split()[:2]
    #key = e1에 value=e2 있으면 반환{e2}/없으면 공집합(set())할당 + {e2} 합집합
    mygraph[e1] = mygraph.setdefault(e1, set()) | {e2}
    #key = e2에 대해서 똑같이
    mygraph[e2] = mygraph.setdefault(e2, set()) | {e1}

# 출력합니다!
print('DFS : ', end='')
dfs(mygraph, "A", set())
print()