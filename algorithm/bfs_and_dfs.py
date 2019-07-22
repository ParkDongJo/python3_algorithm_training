graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
'''
너비 우선 탐색은 깊이가 1인 노드들을 먼저 방문하고 나서, 그 다음에는 깊이가 2인 노드들, 
깊이가 3인 노드들을 차례로 방문하다가 더이상 방문할 곳이 없으면 탐색을 마친다. 
너비 우선 탐색은 그래프 내 모든 노드를 방문하고 싶을 때, 
찾는 것을 발견할 때까지 모든 노드를 적어도 한 번은 방문하고 싶을 때 사용하면 좋다.
'''
def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        n = queue.pop(0)
        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    return visited

# print(bfs(graph, 'A'))
# 기대값 : ['A', 'C', 'B', 'F', 'D', 'E']


'''
너비 우선 경로 탐색을 진행하면 가장 먼저 찾은 경로가 최단 경로가 된다!

'''
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    result = []

    while queue:
        n, path = queue.pop(0)
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                queue.append((m, path + [m]))
    return result

print(bfs_paths(graph, 'A', 'F'))
# 기대값 : [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
print(bfs_paths(graph, 'D', 'F'))
# 기대값 : [['D', 'B', 'E', 'F'], ['D', 'B', 'A', 'C', 'F']]


'''
깊이 우선 탐색은 이름 그대로 진행 가능한 노드가 없을 때까지 깊게 파고들며 방문하는 방식이며, 
더이상 방문 가능한 노드가 없다면 이전의 위치로 돌아와 다른 방향으로 깊게 파고들며 방문한다. 
매우 큰 그래프에서, 탐색을 시작한 노드로부터 너무 멀어지게 되면 즉시 그만두고 싶을 때 사용하면 효과적이다. 
트리 순회 기법은 전부 깊이 우선 탐색이다.

과거 위치의 인접 노드보다 현재 위치의 인접 노드를 먼저 방문한다는 특징을 가지므로, 
아래와 같이 스택(stack)을 사용해 구현할 수 있다.
'''
def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    return visited

# print(dfs(graph, 'A'))
# 기대값 : ['A', 'B', 'E', 'F', 'C', 'D']


'''
깊이 우선 탐색은 너비 우선 탐색과는 달리 최단 경로를 가장 먼저 찾지 못할 수도 있다.
'''
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    result = []

    while stack:
        n, path = stack.pop()
        if n == goal:
            result.append(path)
        else:
            for m in graph[n] - set(path):
                stack.append((m, path + [m]))
    return result

# print(dfs_paths(graph, 'A', 'F'))
# 기대값 : [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
# print(dfs_paths(graph, 'D', 'F'))
# 기대값 : [['D', 'B', 'A', 'C', 'F'], ['D', 'B', 'E', 'F']]
