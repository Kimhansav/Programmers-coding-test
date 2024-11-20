def solution(X, Y):
    x_dict, y_dict, answer = {}, {}, {}
    for i in X:
        if i not in x_dict:
            x_dict[i] = 1
        else:
            x_dict[i] += 1
    for i in Y:
        if i not in y_dict:
            y_dict[i] = 1
        else:
            y_dict[i] += 1
    x_set, y_set = set(i for i in x_dict.keys()), set(i for i in y_dict.keys())    
    x_and_y = x_set & y_set
    print('x_set: ', x_set)
    print('y_set: ', y_set)
    print('x_and_y - set: ', x_and_y - set([0]))
    if len(x_and_y) == 0:
        return '-1'
    if len(x_and_y - (set([0]))) == 0:
        return '0'
    x_and_y = sorted(list(x_and_y), reverse = True)
    answer = ''.join([str(i) * min(x_dict[i], y_dict[i]) for i in x_and_y])
    return answer

print(solution('100', '203045'))