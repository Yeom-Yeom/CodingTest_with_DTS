def solution(numbers,target):
    def dfs(idx, cur_sum):
        # 모든 숫자를 사용한 경우
        if idx==len(numbers):
            # 현재 합계가 타겟 넘버라면 1 반환 아니라면 0 반환
            return 1 if cur_sum==target else 0
        # 현재 숫자를 더하거나, 빼는 두 가지 경우를 탐색
        return dfs(idx+1, cur_sum+numbers[idx])+dfs(idx+1, cur_sum-numbers[idx])
    
    return dfs(0,0)

# dfs 사용