def solution(clothes):
    dict_clothes = {}
    for value, key in clothes:
        if key in dict_clothes.keys():
            dict_clothes[key] += [value]
        else:
            dict_clothes[key] = [value]

    ans = 1

    for _, value in dict_clothes.items():
        ans *= (len(value)+1)

    return ans -1

# key, value = 의상 종류, 의상
# 주어진 2차원 배열을 dictionary로 만들기 위해 for문 이용
# [value]의 값들은 여러 개가 들어갈 수 있으므로 배열을 사용.
# ex) {key: [value1, value2...valueN], ... }
# 의상이 겹치지 않게 입으려면 (N+1)(M+1)
# ans=1로 선언한 이유는 곱셈을 위해서. 이후에 -1을 해준다.