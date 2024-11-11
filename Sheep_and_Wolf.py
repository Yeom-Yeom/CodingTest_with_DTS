from collections import defaultdict, deque
def solution(info, edges):
    # 파이썬에서 트리 구조를 사용하기 위해 자주 사용되는 방식
    tree = defaultdict(list)
    for parent, child in edges:
        tree[parent].append(child)

    # 최대 양의 수를 구하기 위한 변수
    max_sheep = 0

    # dfs 탐색
    def dfs(node, sheep, wolves, next_nodes):
        nonlocal max_sheep
        if info[node] == 0: # 양
            sheep+=1
        else: # 늑대
            wolves+=1
        if wolves >= sheep: # 양의 수가 늑대의 수보다 많아야 함
            return
        max_sheep = max(max_sheep,sheep) # 최대 양의 수를 업데이트

        # 현재 node의 자식들을 next_node에 추가
        for next_node in tree[node]:
            next_nodes.append(next_node)
        
        # 백트래킹 탐색으로, 방문 가능한 노드들을 하나씩 선택하며 dfs를 호출
        for i, next_node in enumerate(next_nodes):
            # 현재 방문한 노드를 제외한 나머지 노드들로 새로운 next_nodes 생성
            dfs(next_node, sheep, wolves, next_nodes[:i]+next_nodes[i+1:])

    # 루트노드, 양=0, 늑대=0, 비어있는 next_nodes에서 시작.
    dfs(0,0,0,[])

    return max_sheep

# dfs 방식, 백트래킹
# defaultdict는 트리 구조를 표현하기 위해 사용, 기본적으로 비어있는 리스트를 값으로 가지는 딕셔너리 형태로 트리를 구성
# dfs에서 max_sheep에 nonlocal을 안붙히면 error, nonlocal에 대한 설명 하단 링크
# https://daleseo.com/python-global-nonlocal/
