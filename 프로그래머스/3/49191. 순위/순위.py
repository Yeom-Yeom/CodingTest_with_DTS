def solution(n, results):
    graph = [[False] * (n+1) for _ in range(n+1)] # 그래프 생성
    for win, lose in results:
        graph[win][lose] = True # 경기 결과 그래프에 기록

    for k in range(1,n+1): # 경유 노드
        for i in range(1,n+1): # 출발 노드
            for j in range(1,n+1): # 도착 노드
                if graph[i][k] and graph[k][j]: 
                    graph[i][j] = True
    
    # 각 선수에 대해 
    answer = 0
    for i in range(1,n+1):
        cnt = 0
        for j in range(1,n+1):
            if graph[i][j] or graph[j][i]: # 둘 중 하나가 이겼으면
                cnt+=1
        if cnt == n-1: # 다른 모든 선수와 승패가 정해진 경우
            answer +=1
    return answer

# 플로이드-워셜 알고리즘
# https://velog.io/@kimdukbae/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Floyd-Warshall-Algorithm
