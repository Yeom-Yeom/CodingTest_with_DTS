
from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0 # 경과 시간
    bridge = deque([0]*bridge_length) # 다리를 지나는 트럭
    truck_weights = deque(truck_weights) # 트럭을 deque로 변경

    cur_weight = 0 # 현재 다리 위 트럭들의 총 무게
    truck_idx = 0 # 다리를 지나가는 트럭의 인덱스

    # 차량이 지날 수 있거나 현재 다리 위에 트럭이 없다면
    while truck_idx < len(truck_weights) or cur_weight > 0:
        time += 1
        # 다리에서 트럭이 하나 나가는 경우
        truck = bridge.popleft()
        cur_weight -= truck

        # 새로운 트럭이 다리 위에 올라갈 수 있는지 확인
        if truck_idx < len(truck_weights):
            if cur_weight + truck_weights[truck_idx] <= weight:
                # 트럭이 다리에 올라가라 수 있다면 다리에 index 위치의 트럭을 추가
                bridge.append(truck_weights[truck_idx])
                cur_weight += truck_weights[truck_idx]
                truck_idx +=1
            else:
                # 다리에 트럭이 올라갈 수 없다면 0을 넣어 대기
                bridge.append(0)
    return time

# 다리에 올라갈 수 없을 때, 경과 시간을 +1 해야 하는지에 대해 고민하고 풀어보다가
# 실패가 되어 gpt의 도움을 받았읍니다.. [0] 인덱스를 채워 대기를 시켜주더군요.
# 시간 복잡도 : while문 1번, O(n)
# 공간 복잡도 : 다리 상태를 관리하는 큐 bridge의 크기, O(bridge_length)