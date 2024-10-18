def solution(num_list,n):
    answer = [[0 for i in range(n)] for j in range(len(num_list)//n)]
    tmp = 0
    for i in range(len(num_list)//n):
        for j in range(n):
            answer[i][j] = num_list[tmp]
            tmp+=1
    return answer

print(solution([1,2,3,4,5,6,7,8],2))