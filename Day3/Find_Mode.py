## 해당 문제는 시간 복잡도를 고려하여 다시 풀어 볼 수 있음.


def solution(array):
    count = {} # key-value dictionary
               # key : array원소, value : array원소 빈도 수 

    # 딕셔너리 초기화
    # 배열 전체를 조회하여 키 값과 비교 후, 이미 키 값이 있으면
    # 해당 key 값에 맞는 value에 +1
    # 존재하지 않는다면 새로 추가
    for i in array:
        if i not in count.keys():
            count[i] = 1
        else:
            count[i] = count.get(i)+1
        
    temp = sorted(count.values()) # 최빈값을 구하기 위해 정렬
    max_count = temp[(len(count.keys())-1)] # 오름차순 기준으로 가장 마지막 값이 최빈값
    cnt = 0 # 최빈값이 두 개 이상 존재하는지 판별하기 위한 변수

    for i,j in count.items(): # key-value에서 value 값이 최빈값이라면, cnt+1, 해당 키 값이 최빈값
        if j == max_count:
            cnt+=1
            answer = i

    if cnt == 1:
        return answer
    else:
        return -1 # 최빈값이 두 개 이상이라면 문제 조건에 따라 -1 return.
        
print(solution([1,1,2,2,3,3,3,4]))