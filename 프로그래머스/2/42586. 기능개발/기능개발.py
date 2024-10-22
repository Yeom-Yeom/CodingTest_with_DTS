from math import ceil

def solution(progresses, speeds):
    answer = []
    days = []  # 각 작업이 끝나기까지 남은 일수를 저장할 리스트
    
    # 각 작업의 남은 일수를 계산
    for i in range(len(progresses)):
        remaining_days = ceil((100 - progresses[i]) / speeds[i])
        days.append(remaining_days)
    
    # 첫 번째 작업이 끝나기까지 걸리는 일수를 기준으로 설정
    current_deploy = days[0]
    count = 0  # 현재 배포에서 처리할 기능 개수
    
    for day in days:
        if day <= current_deploy:
            count += 1  # 현재 기능이 함께 배포 가능하면 count 증가
        else:
            # 새로운 배포 시작
            answer.append(count)  # 지금까지 함께 배포된 기능 수 추가
            current_deploy = day  # 새로운 기준 일수로 변경
            count = 1  # 새롭게 시작하는 배포는 1개로 시작
    
    answer.append(count)  # 마지막으로 남은 배포 추가
    
    return answer