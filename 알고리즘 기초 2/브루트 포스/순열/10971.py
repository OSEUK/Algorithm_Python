# 백준 10971, 외판원 순회 2 (SILVER II)
# Traveling Salesman problem
 
# 현재 마을, 시작 마을, 현재 비용
def tsp(curr_city, start, curr_cost):
    # 순회 끝나면
    if start == curr_city and False not in visited:
        cost = curr_cost
        result.append(cost)
        return
    
    # 방문한 적 없는 다른 도시
    for i in range(N):
        if arr[curr_city][i] != 0 and not visited[i]:
            visited[i] = True
            tsp(i, start, curr_cost + arr[curr_city][i])
            visited[i] = False
    
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [False]*N
result = []

tsp(0, 0, 0)
print(min(result))