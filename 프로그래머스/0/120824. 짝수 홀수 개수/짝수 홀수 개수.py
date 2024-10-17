def solution(num_list):
    ans = [0,0]
    for n in num_list:
        if n%2==0:
            ans[0]+=1
        else:
            ans[1]+=1
    return ans