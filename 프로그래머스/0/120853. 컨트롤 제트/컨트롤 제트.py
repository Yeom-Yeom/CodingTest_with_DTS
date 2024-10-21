def solution(s):
    stack = []
    for i in s.split(' '):
        if i != 'Z':
            stack.append(int(i)) # 주어진 s는 문자열이므로 i를 int형으로 변환
        else:
            stack.pop() # 'Z'라면 stack에서 pop
    return sum(stack)   # 남은 stack의 합


# ex) s="10 20 Z 30"
# ' '로 구분되어 있으므로 split(' ')을 통해 각 문자를 구분
# stack = [10] -> stack = [10,20] -> i='Z' -> stack = [10] -> stack = [10,30]
# sum(stack) = 10+30 = 40
