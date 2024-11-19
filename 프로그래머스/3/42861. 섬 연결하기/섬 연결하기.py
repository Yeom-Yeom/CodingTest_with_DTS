def solution(n, costs):
    ans = 0
    costs.sort(key=lambda x:x[2]) # 경로 비용이 적은 순으로 정렬
    link = set([costs[0][0]]) # 시작점
    
    # kruskal 알고리즘
    while len(link) != n: # 모든 위치가 연결될 때 까지
        for v in costs:
            if v[0] in link and v[1] in link: # 두 섬이 이미 낮은 비용으로 연결되었을 경우 무시
                continue
            if v[0] in link or v[1] in link: # 두 섬 중 하나가 현결되어있지 않을 때
                link.update([v[0],v[1]]) # 섬 연결 후
                ans += v[2] # 비용 더하기
                break
    return ans