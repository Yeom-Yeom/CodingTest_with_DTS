def solution(cards1, cards2, goal):
    answer = "Yes" # default = Yes
    
    cards1_idx , cards2_idx = 0,0 # cards1, cards2의 인덱스

    for card in goal:
        if len(cards1) > cards1_idx and card == cards1[cards1_idx]:
            # 인덱스가 cards1의 길이보다 작고, 해당 인덱스 위치의 값이 card와 같다면, 인덱스 증가
            cards1_idx+=1
        elif len(cards2) > cards2_idx and card == cards2[cards2_idx]:
            # cards1에 존재하지 않는다면, cards2에서 비교
            cards2_idx+=1
        else: # 순서대로 진행했을 때 존재하지 않는다면, No를 반환. 반복문을 더이상 돌릴 필요 없으므로 break
            answer = "No"
            break
    return answer