from collections import defaultdict
def solution(tickets):
    # 그래프 생성
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end) # 출발 공항에서, 도착 공항 기록

    # 각 출발 공항에서의 도착 공항 리스트를 알파벳 역순으로 정렬
    # 역순 정렬 이유: dfs에서 스택 구조로 인해 가장 나중에 들어온 공항이 먼저 처리되기 때문
    for key in graph:
        graph[key].sort(reverse=True)
    answer=[]

    def dfs(route):
        # 가능한 경로 모두 탐색
        while graph[route]:
            # 도착 공항 중 가장 마지막(알파벳 순서로 가장 작은)을 선택
            next_route = graph[route].pop()
            dfs(next_route) # 그 다음 공항에서 다시 출발
        # 더 이상 갈 곳이 없으면 해당 공항을 추가
        answer.append(route)

    dfs("ICN")
    # 탐색이 끝난 후에는 경로가 역순으로 저장되어있으므로, 다시 역순으로 반환
    return answer[::-1]