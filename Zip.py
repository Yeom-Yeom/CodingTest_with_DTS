def solution(msg):
    alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    dict = {k:v for (k,v) in zip(alphabet,list(range(1,27)))}
    # (key,value) dictionary 를 zip함수를 통해 k=alphabet, v = 1~26
    
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

# msg가 dictionary에 있으면