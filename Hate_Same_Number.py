def solution(arr):
    answer = []
    answer.append(arr[0]) # 맨 처음 숫자 추가
    for i in range(1,len(arr)): # 두 번째 숫자부터 arr 길이만큼
        if arr[i] != answer[-1]: # 가장 마지막에 추가한 값과 동일하지 않다면
            answer.append(arr[i]) # 해당 값 추가
    return answer 

print(solution([1,1,3,3,0,1,1]))