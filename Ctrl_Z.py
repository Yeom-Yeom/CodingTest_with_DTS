def solution(s):
    stack = []
    for i in s.split(' '):
        if i != 'Z':
            stack.append(int(i)) # 주어진 s는 문자열이므로 i를 int형으로 변환
        else:
            stack.pop() # 'Z'라면 stack에서 pop
    return sum(stack)   # 남은 stack의 합
