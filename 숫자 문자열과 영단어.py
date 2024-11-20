import re

def solution(s):
    answer = 0
    eng_num_dict = {'zero' : '0', 'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5', 'six' : '6', 'seven' : '7', 'eight' : '8', 'nine' : '9'}
    for item in eng_num_dict.items():
        p = re.compile(fr'{item[0]}')
        s = p.sub(item[1], s)
    print('answer before int(): ', s)
    s = int(s)
    return s

print(solution("one4seveneight"))

item = ['zero', 'one', 'two']