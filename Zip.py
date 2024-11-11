def solution(msg):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dict = {}
    
    # {'A':1,'B':2...'Z':26}
    for i in range(len(alphabet)):
        dict[alphabet[i]]= i+1
    
    ans = []
    while True:
        if msg in dict:
            ans.append(dict[msg])
            break
        for i in range(1,len(msg)+1):
            if msg[0:i] not in dict:
                ans.append(dict[msg[0:i-1]])
                dict[msg[0:i]] = len(dict)+1
                msg = msg[i-1:]
                break
    return ans

# msg가 dictionary에 있으면 ans에 dict[msg]에 해당하는 번호 추가
# 없다면, 1부터 msg의 길이까지
# 만약 앞에서 부터 i번째 까지 dict에 없다면
# ans에 추가,해당 번호는 length+1 
# break로 for문 종료
# 모든 문자가 존재한다면 while문 break