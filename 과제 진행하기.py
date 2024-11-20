#0. 남은 게 마지막 과목 -> 이번 거 끝내기, 대기과목 역순으로 끝내기
#1. 시간 남아서 끝내기(끝난시간 < 다음시작시간) -> 이번 거 종료, 최근에 멈춘 거 시작
#2. 시간 모자라서 새거시작(끝난시간 > 다음시작시간) -> 이번 거 보류, 다음거 새거시작
#3. 시간 맞춰 끝냈는데 새거 남은거 다 있어서 새거시작(끝난시간 == 다음시작시간) -> 이번 거 종료, 다음거 새거시작

def solution(plans):
    answer = []
    for plan in plans:
        hour, minute = int(plan[1].split(':')[0]), int(plan[1].split(':')[1])
        plan[1] = 60 * hour + minute
    plans.sort(key = lambda x: x[1])
    print('plans: ', plans)
    todo_dict = {x[0] : {'index' : plans.index(x), 'start' : x[1], 'time_left' : int(x[2])} for x in plans}
    todo_list = [x[0] for x in plans]
    length = len(todo_list)
    todo = todo_list.pop(0)
    cur_time = todo_dict[todo]['start']
    next_time = todo_dict[todo_list[0]]['start']
    wait_list = []
    print('length: ', length)

    while len(answer) < length:
        print('answer: ', answer)
        print('wait_list: ', wait_list)
        print('todo list: ', todo_list)
        print('cur time: ', cur_time)
        print('next time: ', next_time)
        print('todo: ', todo)
        if len(todo_list) == 0: #남은 게 마지막거
            answer.append(todo)
            if len(wait_list) != 0:
                wait_list.reverse()
                answer += wait_list
        elif todo_dict[todo]['time_left'] < next_time - cur_time: #시간 남는 경우
            answer.append(todo)
            cur_time += todo_dict[todo]['time_left']
            todo_dict[todo]['time_left'] = 0

            if len(wait_list) != 0: #대기과제 시작
                todo = wait_list.pop()
            else: #다음 새 과제 시작
                todo = todo_list.pop(0)
                cur_time = next_time
                if len(todo_list) != 0:
                    next_time = todo_dict[todo_list[0]]['start']

            print('todo and next time: ', todo, next_time)

        elif todo_dict[todo]['time_left'] > next_time - cur_time: #시간 부족으로 다음 거 시작하는 경우
            wait_list.append(todo)
            todo_dict[todo]['time_left'] -= (next_time - cur_time)
            cur_time = next_time
            todo = todo_list.pop(0)

            if len(todo_list) != 0:
                next_time = todo_dict[todo_list[0]]['start']

            print('todo and next time: ', todo, next_time)

        else: #시간 딱 맞춰서 다음 거 시작하는 경우
            answer.append(todo)
            todo_dict[todo]['time_left'] = 0
            cur_time = next_time
            todo = todo_list.pop(0)

            if len(todo_list) != 0:
                next_time = todo_dict[todo_list[0]]['start']

            print('todo and next time: ', todo, next_time)

    return answer

print(solution([["korean", "11:40", "30"], ["english", "12:10", "20"], ["math", "12:30", "40"]]))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "14:00", "30"], ["computer", "12:30", "100"]]	))
print(solution([["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]	))
print(solution([["aaa", "12:00", "200"], ["bbb", "12:30", "10"], ["ccc", "12:40", "10"], ["ddd", "13:10", "10"], ["eee", "13:30", "10"]]))
print(solution([["aaa", "12:00", "20"], ["bbb", "12:30", "20"], ["ccc", "12:40", "10"], ["ddd", "13:10", "30"], ["eee", "13:40", "10"]]))
print(solution([["science", "12:40", "50"], ["music", "12:20", "40"], ["history", "15:00", "30"], ["computer", "12:30", "100"]]))
