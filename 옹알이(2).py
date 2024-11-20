def solution(babbling):
    answer = 0
    candid = ['aya', 'ye', 'woo', 'ma']
    for i in babbling:
        sep_list = []
        query = ''
        last_add = ''
        for char in i:
            query += char
            if query != last_add and query in candid:
                
                sep_list.append(query)
                last_add = query
                query = ''
            
        if ''.join(sep_list) == i:
            answer += 1
    return answer

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))