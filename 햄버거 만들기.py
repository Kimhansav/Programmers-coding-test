def solution(ingredient):
    answer = 0
    new_list = []
    for i in ingredient:
        new_list.append(i)
        if new_list[-4:] == [1, 2, 3, 1]:
            #시간 초과 방지를 위해 슬라이싱 대신 del이나 pop사용. 
            del new_list[-4:]
            answer += 1
    return answer

