def solution(hp):
    ans = 0
    ans += hp//5
    hp%=5
    ans+=hp//3
    hp%=3
    ans+=hp
    return ans