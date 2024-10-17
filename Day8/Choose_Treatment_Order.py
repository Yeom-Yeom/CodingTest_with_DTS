def solution(emergency):
    tmp = sorted(emergency,reverse=True)
    ans = []
    for i in emergency:
        ans.append(tmp.index(i)+1)
    return ans
