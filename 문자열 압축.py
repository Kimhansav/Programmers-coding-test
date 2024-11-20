import re

def solution(s):
    answer = 0
    if len(s) == 1:
        return 1
    for i in range(1, len(s) // 2 + 1):
        string = s
        j = 0
        length = 0
        while j < len(s):
            print('i: ', i)
            print('j: ', j)
            print('str part: ', string[j:j + i])
            cur_pattern = re.compile(f'({string[j:j + i]})+')
            print('cur_pattern: ', cur_pattern)
            result = cur_pattern.match(string[j:])
            print('result :', result)
            print('result start: ', result.start())
            print('result end: ', result.end())
            if i >= len(s) - j:
                length += len(s) - j
                j  = len(s)
            elif result.end() != i:
                print('str((result.end() - result.start()) / i): ', str(int((result.end() - result.start()) / i)))
                length += (len(str(int((result.end() - result.start()) / i))) + i)
                j += result.end()
            else:
                length += i
                j += i
            print('length: ', length)
        if answer == 0:
            answer = length
        else:
            if answer > length:
                answer = length
        print('answer: ', answer)
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("a"))