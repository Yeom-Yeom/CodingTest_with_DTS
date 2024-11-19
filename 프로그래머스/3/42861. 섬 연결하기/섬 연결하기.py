# 노드가 포함되어 있는지 찾는 함수
def find_node(sets, node):
    for s in sets:
        if node in s:
            return s
    return None


def solution(n, costs):
    costs.sort(key=lambda x: x[2])

    # 각 섬을 set을 포함한 list로 초기화
    sets = [set([i]) for i in range(n)]
    total_cost = 0


    for node1, node2, cost in costs:
        # 각 섬이 속한 노드 찾기 이때 n1, n2는 sets의 원소를 참조 해서 저장
        # 포인트의 개념?
        n1 = find_node(sets, node1)
        n2 = find_node(sets, node2)


        # n1, n2 중 하나만 존재할 때
        if n1 != n2:
            n1.update(n2) # n1에 n2를 업데이트 하면 sets의 원소도 바뀜
            sets.remove(n2) # n1에 n2를 포함 시키고 개별 원소로 존재하는 n2 제거
            total_cost += cost

            print("---------------------------")

        # 모든 섬이 하나의 집합으로 통합되었으면 종료
        if len(sets) == 1:
            break

    return total_cost