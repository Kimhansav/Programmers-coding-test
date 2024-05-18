def solution(today, terms, privacies):
    answer = []
    today_y, today_m, today_d = int(today.split('.')[0]), int(today.split('.')[1]), int(today.split('.')[2])
    expire_period_dict = {term.split(' ')[0] : int(term.split(' ')[1]) for term in terms}        
    for index, info in enumerate(privacies):
        info_start_y, info_start_m, info_start_d = int(info.split(' ')[0].split('.')[0]), int(info.split(' ')[0].split('.')[1]), int(info.split(' ')[0].split('.')[2])
        info_name = info.split(' ')[1]
        info_expire_y = info_start_y + (info_start_m + expire_period_dict[info_name]) // 12 if (info_start_m + expire_period_dict[info_name]) % 12 != 0 else (info_start_y + (info_start_m + expire_period_dict[info_name]) // 12) - 1
        info_expire_m = (info_start_m + expire_period_dict[info_name]) % 12 if (info_start_m + expire_period_dict[info_name]) % 12 != 0 else 12
        if info_start_d == 1:
            info_expire_d = 28
            if info_expire_m == 1:
                info_expire_m = 12
                info_expire_y -= 1
            else:
                info_expire_m -= 1
        else:
            info_expire_d = info_start_d - 1 
                
        if (today_y > info_expire_y) or (today_y == info_expire_y and today_m > info_expire_m) or (today_y == info_expire_y and today_m == info_expire_m and today_d > info_expire_d):
            answer.append(index + 1)
    return answer