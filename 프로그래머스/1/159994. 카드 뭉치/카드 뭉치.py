# def solution(cards1, cards2, goal):
#     answer = "Yes" # default = Yes
    
#     cards1_idx , cards2_idx = 0,0 # cards1, cards2의 인덱스

#     for card in goal:
#         if len(cards1) > cards1_idx and card == cards1[cards1_idx]:
#             # 인덱스가 cards1의 길이보다 작고, 해당 인덱스 위치의 값이 card와 같다면, 인덱스 증가
#             cards1_idx+=1
#         elif len(cards2) > cards2_idx and card == cards2[cards2_idx]:
#             # cards1에 존재하지 않는다면, cards2에서 비교
#             cards2_idx+=1
#         else: # 순서대로 진행했을 때 존재하지 않는다면, No를 반환. 반복문을 더이상 돌릴 필요 없으므로 break
#             answer = "No"
#             break
#     return answer

from collections import deque
def solution(cards1, cards2, goal):
    answer = "Yes"
    deq1 = deque(cards1) # cards1을 deque로 변환하기 위한 변수
    deq2 = deque(cards2) # cards2를 deque로 변환하기 위한 변수

    # for i in cards1: # cards1의 원소를 deq1로 append
    #     deq1.append(i)

    # for i in cards2: # cards2의 원소를 deq2로 append
    #     deq2.append(i)
    
    for card in goal:
        if deq1 and card == deq1[0]:
            deq1.popleft()
        elif deq2 and card == deq2[0]:
            deq2.popleft()
        else:
            answer = "No"
            break
    return answer

print(solution(["i", "drink", "water"],["want", "to"],["i", "want", "to", "drink", "water"]))