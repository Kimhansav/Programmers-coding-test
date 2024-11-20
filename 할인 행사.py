def solution(want, number, discount):
    answer = 0
    buying_dict = {name : quantity for name, quantity in zip(want, number)}
    for i in range(0, len(discount) - 9):
        cur_dict = {name : 0 for name in want}
        days = discount[i : i + 10]
        if set(days) != set(buying_dict.keys()):
            continue
        for item in days:
            cur_dict[item] += 1
        if buying_dict.items() == cur_dict.items():
            answer += 1
    return answer