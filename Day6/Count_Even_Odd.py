def solution(num_list):
    ans = [0,0]
    for n in num_list:
        ans[n%2]+=1
    return ans