# 첫 풀이 시간 초과
# 
from collections import deque
def solution(queue1, queue2):
    deq1 = deque(queue1)
    deq2 = deque(queue2)
    sum1 = sum(deq1)
    sum2 = sum(deq2)
    total_sum = sum1 + sum2

    if total_sum % 2 != 0:
        return -1

    target = total_sum //2
    max_operation = (len(deq1)+ len(deq2))*2 # 최대 작업 횟수
 
    count = 0
    

    while sum1 != target:
        if sum1 > target:
            value = deq1.popleft()
            sum1 -=value
            deq2.append(value)
            sum2+=value
        else:
            value = deq2.popleft()
            sum2 -= value
            deq1.append(value)
            sum1+=value
        count+=1

        if count > max_operation:
            return -1

    return count