# 첫 풀이 시간 초과
# 
from collections import deque
def solution(queue1, queue2):
    deq1 = deque(queue1) # deque로 만들기
    deq2 = deque(queue2) # deque로 만들기
    sum1 = sum(deq1) 
    sum2 = sum(deq2)
    total_sum = sum1 + sum2

    if total_sum % 2 != 0: # 두 큐의 합을 나눌 수 없으면 -1 return
        return -1

    target = total_sum //2 # target = 두 큐의 합 // 2
    max_operation = (len(deq1)+ len(deq2))*2 # 최대 작업 횟수
    # deq1이 두 번 반복되고, deq2가 두 번 반복되면 만들지 못함
 
    count = 0
    

    while sum1 != target: # deq1의 합이 target이 아닐 경우, 즉 두 큐 합이 같지 않을 때
        if sum1 > target: # target보다 크다면,
            value = deq1.popleft() # deq1에서 원소를 빼, deq2로 넣음
            sum1 -=value # deq1에서 빠진 원소의 값을 고려하여, sum1을 갱신
            deq2.append(value)
            sum2+=value # deq1에서 넘어온 값을 고려하여, sum2를 갱신
        else:
            value = deq2.popleft()
            sum2 -= value
            deq1.append(value)
            sum1+=value
        count+=1 # 작업 횟수 증가

        if count > max_operation: # 
            return -1

    return count