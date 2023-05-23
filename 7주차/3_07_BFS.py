# 필요한 모듈을 추가해 보세요!
from queue import Queue 
visited = []

# 1번을 해보세요!
def bfs(graph, start):
    startqueue = Queue()
    
    # 시작점 큐에 넣음
    startqueue.put(start)
    while not startqueue.empty():

        # 큐에서 제일 앞 뺌
        newstart = startqueue.get()

        visited.append(newstart)
        # start와 인접한 정점 중 안에 안 들어있는거 모두 넣기
        for u in graph[newstart]:
            if u not in startqueue.queue and u not in visited:
                startqueue.put(u)
    
    for v in range(len(visited)) :
        print(visited[v], end=" ")
    
# 2번을 해보세요!
mygraph = dict()
#간선의 개수
n = int(input())

for _ in range(n) : 
    e1, e2 = input().split()[:2]
    mygraph[e1] = mygraph.setdefault(e1, set()) | {e2}
    mygraph[e2] = mygraph.setdefault(e2, set()) | {e1}

# 출력합니다!
print('BFS : ', end='')
bfs(mygraph, "A")
print()