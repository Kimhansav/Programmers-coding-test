def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reporter_reported_dict = {name : set() for name in id_list}
    reported_reporter_dict = {name : set() for name in id_list}
    for item in report:
        content = item.split(' ')
        reported_reporter_dict[content[1]].add(content[0])
        reporter_reported_dict[content[0]].add(content[1])
    for index, item in enumerate(reporter_reported_dict.values()):
        for name in list(item):
            if len(reported_reporter_dict[name]) >= k:
                answer[index] += 1
    return answer