def solution(friends, gifts):
    answer = 0
    chart = {giver : {receiver : 0 for receiver in friends} for giver in friends}
    rate = {name : {'give' : 0, 'receive' : 0} for name in friends}
    result = {name : 0 for name in friends}
    for item in gifts:
        content = item.split(' ')
        chart[content[0]][content[1]] += 1
        rate[content[0]]['give'] += 1
        rate[content[1]]['receive'] += 1
    for name1 in friends:
        for name2 in friends:
            if chart[name1][name2] > chart[name2][name1]:
                result[name1] += 1
            elif chart[name1][name2] == chart[name2][name1] and (rate[name1]['give'] - rate[name1]['receive']) > (rate[name2]['give'] - rate[name2]['receive']):
                result[name1] += 1
    answer = max(result.values())
    return answer