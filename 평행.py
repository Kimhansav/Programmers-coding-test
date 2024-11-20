def solution(dots):
    answer = 0
    point, left = dots[0], dots[1:]
    print('left: ', left)
    for i in range(len(left)):
        print('left[i]: ', left[i])
        first, second = [point, left[i]], left.remove(left[i])
        print('first:', first)
        print('second:', second)
        if (first[1][1] - first[0][1]) / (first[1][0] - first[0][0]) == (second[1][1] - second[0][1]) / (second[1][0] - second[0][0]):
            return 1
        print(left)
    return answer

print(solution([[1, 4], [9, 2], [3, 8], [11, 6]]))