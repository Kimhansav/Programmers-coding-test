import re

def solution(new_id):
    answer = ''
    #1단계
    answer = new_id.lower()
    print('1단계: ', answer)
    #2단계
    pattern = re.compile('[a-z0-9_.-]')
    for item in answer:
        if not pattern.match(item):
            answer = answer.replace(item, '')
    print('2단계: ', answer)
    #3단계
    pattern = re.compile('[.]{2,}')
    result = pattern.findall(answer)
    for object in result:
        answer = answer.replace(object, '.')
    print('3단계: ', answer)
    #4단계
    if answer[0] == '.':
        answer = answer[1:]
    if len(answer) != 0 and answer[-1] == '.':
        answer = answer[:-1]
    #5단계
    if len(answer) == 0:
        answer = 'a'
    #6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    #7단계
    if len(answer) <= 2:
        add_char = answer[-1]
        for i in range(3 - len(answer)):
            answer += add_char
    
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
print(solution("b=.=.=.=.=.=.=.=.=.=.=.=.=.=.=.x"))
print(solution("a....a....a"))
print(solution("b..!a"))

