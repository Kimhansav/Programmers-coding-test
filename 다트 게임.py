def solution(dartResult):
    answer = 0
    score_candid = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    sep_list = []
    score_result = []
    for i in range(len(dartResult)):
        if len(sep_list) == 2:
            sep_list.append(dartResult[i:])
            break
        if dartResult[i+1] in score_candid:
            sep_list.append(dartResult[:i+1])
    for trial in sep_list:
        bonus_idx = 0
        for i in range(len(trial)):
            if trial[i].isalpha():
                bonus_idx = i
        cur_option = trial[bonus_idx + 1] if bonus_idx + 1 < len(trial) else None
        score_result.append({'score':int(trial[:bonus_idx]), 'bonus':trial[bonus_idx], 'option':cur_option})
    for i in range(3):
        cur_score, cur_bonus, cur_option = score_result[i]['score'], score_result[i]['bonus'], score_result[i]['option']
        if cur_bonus == 'S':
            pass
        elif cur_bonus == 'D':
            cur_score **= 2
        elif cur_bonus == 'T':
            cur_score **= 3
        
        if i < 2 and score_result[i+1]['option'] == '*':
            cur_score *= 2
        if cur_option == '*':
            cur_score *= 2
        elif cur_option == '#':
            cur_score *= -1
            
            
        answer += cur_score
    return answer

print(solution('1T2D3D#'))