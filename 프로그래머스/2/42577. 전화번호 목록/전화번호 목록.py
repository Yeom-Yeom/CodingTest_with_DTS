def solution(phone_book):
    hash_map = {}
    for phone in phone_book:
        hash_map[phone] = 1 # {each phone:1}

    for phone in phone_book:
        arr=""
        for p in phone:
            arr+=p # arr에 phone 번호 추가

            if arr in hash_map and arr!= phone: # 만약 arr에 존재하고, 자기 자신의 값이 아니라면
                return False # 존재하는 것이므로 False
    return True