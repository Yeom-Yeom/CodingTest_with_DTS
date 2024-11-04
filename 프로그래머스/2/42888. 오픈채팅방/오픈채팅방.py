def solution(record):
    dict = {}
    answer = []
    for rec in record:
        tmp = rec.split() # 각 레코드를 공백으로 구분
        if tmp[0] != "Leave": # Enter 또는 Change인 경우 
            # uid에 해당 하는 값을 name으로 갱신하거나 없다면 추가
            dict[tmp[1]] = tmp[2] # uid = key, name = value
    for rec in record:
        tmp = rec.split()
        if tmp[0] == "Enter":
            answer.append(f"{dict[tmp[1]]}님이 들어왔습니다.")
        elif tmp[0] == "Leave":
            answer.append(f"{dict[tmp[1]]}님이 나갔습니다.")

    return answer