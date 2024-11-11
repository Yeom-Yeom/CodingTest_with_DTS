def solution(n, times):
    left = 1
    right = max(times)*n
    ans = right

    while left <= right:
        mid = (left+right)//2
        people = sum(mid // time for time in times)

        if people>=n:
            ans=mid
            right = mid-1
        else:
            left = mid+1

    return ans

# 이진 탐색
# left(최소 시간 1분), right(최대 시간 times의 max값을 n명이 걸렸을 때)
# mid = 중간 값 
# 각 심사관이 중간 값의 시간 동안 심사할 수 있는 인원 수 계산
# people이 n명 이상이면, ans = mid로 업데이트를 통해 최소 시간 유지
# ex) n=6, times=[7,10]에서 left=1, right=60, mid = 30
# ex) people = (30//7 + 30//10) = 7
# ex) 7>=6이므로 최소 시간을 더 줄인다.
# right=mid-1 로 설정, left ~ mid-1에서 확인.