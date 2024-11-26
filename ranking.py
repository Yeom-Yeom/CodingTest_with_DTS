def solution(n, results):
    graph = [[False] * (n+1) for _ in range(n+1)] # 그래프 생성
    for win, lose in results:
        graph[win][lose] = True # 경기 결과 그래프에 기록

    for k in range(1,n+1): # 경유 노드
        for i in range(1,n+1): # 출발 노드
            for j in range(1,n+1): # 도착 노드
                # 만약 i가 k를 이기고, k가 j를 이긴다면 i는 j를 이길 수 있음
                if graph[i][k] and graph[k][j]: 
                    graph[i][j] = True
    
    # 각 선수에 대해 
    answer = 0
    for i in range(1,n+1):
        cnt = 0
        for j in range(1,n+1):
            if graph[i][j] or graph[j][i]: # 둘 중 하나가 이겼으면
                cnt+=1
        if cnt == n-1: # 자신을 제외한 다른 모든 선수와 승패가 정해진 경우
            answer +=1
    return answer

# graph[i][j] 는 i가 j를 이길 수 있음을 의미.
# 모든 선수에 대해 자신을 제외한 n-1명과 승패가 확정된 경우 순위를 알 수 있음.
# 플로이드-워셜 알고리즘
# https://velog.io/@kimdukbae/%ED%94%8C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%9B%8C%EC%85%9C-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Floyd-Warshall-Algorithm
# n의 갯수가 100까지로 O(n^3) 이더라도, 큰 시간이 걸리지 않음.
