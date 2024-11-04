def solution(n):
    ans = 0
    while True:
        ans+=1
        if n/ans <1:
            break
        else:
            n/=ans
    return ans-1