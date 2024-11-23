def solution(n, words):
    answer = [0,0]

    cnt = 0
    checks = []
    checks.append(words[0]) # 첫 번째 문자 추가
    for i in range(1, len(words)): # 모든 문자열에 대해서
        cnt+=1
        # 이미 말한 단어가 아니고, 말한 단어의 마지막 글자로 시작한다면
        if words[i] not in checks and list(words[i-1])[-1] == list(words[i])[0] :
            checks.append(words[i])
        # 그 외에
        else:
            answer[0] = cnt%n+1 # 탈락한 사람의 번호
            answer[1] = cnt//n+1 # 몇 번째로 탈락했는지
            break
    return answer