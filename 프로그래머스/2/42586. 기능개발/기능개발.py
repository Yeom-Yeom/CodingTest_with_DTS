from math import ceil
from collections import deque

# def solution(progresses, speeds):
#     answer = []
#     days = []  # 각 작업이 남은 일수 저장 리스트
    
#     # 각 작업의 남은 일수를 계산
#     # ceil을 통해 소수점 올림. 소수점이 존재한다면 하루 더 걸린다는 것.
#     for i in range(len(progresses)):
#         tmp = ceil((100 - progresses[i]) / speeds[i])
#         days.append(tmp)
    
#     # 첫 번째 작업이 끝나기까지 걸리는 일수를 기준으로 설정
#     cur_deploy = days[0]
#     count = 0  # 현재 배포에서 처리할 기능 개수
    
#     for day in days:
#         if day <= cur_deploy:
#             count += 1  # 현재 기능이 함께 배포 가능하면 count 증가
#         else:
#             # 새로운 배포
#             answer.append(count)  # 지금까지 함께 배포된 기능 수 추가
#             cur_deploy = day  # 새로운 기준 일수로 변경
#             count = 1  # 새롭게 시작하는 배포는 1개로 시작
    
#     answer.append(count)  # 마지막으로 남은 배포 추가
    
#     return answer

# deque 로 풀었을 때
def solution(progresses, speeds):
    answer = []
    deq = deque()

    for i in range(len(progresses)):
        tmp = ceil((100-progresses[i])/speeds[i])
        deq.append(tmp)

    while deq:
        cur_deploy = deq.popleft()
        count = 1

        while deq and deq[0] <= cur_deploy:
            deq.popleft()
            count+=1
        answer.append(count)
    return answer

# 둘 다 시간복잡도 O(n), 공간 복잡도 O(n)
# deque를 사용하는 방식은 내부적으로 더 많은 메모리를 사용하게 된다.
# deque의 특성 상 리스트보다 추가적인 메모리를 차지할 수 있음(-chatGPT)
# 공간 복잡도 측면에서 인덱스를 사용하는 방식이 좀 더 효율적
