def solution(s):
    tmp = []
    for c in s:
        if c=='(':
            tmp.append('(') # 주어진 문자열 에서 '('가 존재한다면 스택에 추가.
        else:
            if '(' in tmp: # ')' 값이 주어지고, 스택에 '('가 있다면, '('값을 pop()
                tmp.pop()
            else: # ')' 값이 들어왔지만, 스택에 '('이 없다면 잘못된 괄호로 False return
                return False
    if len(tmp) == 0: # 올바르게 들어왔다면 append, pop의 갯수가 동일하므로 길이가 0이 되어야함
        return True
    else:
        return False
    
print(solution(")()()"))