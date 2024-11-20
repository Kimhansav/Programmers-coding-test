#n이 2면 3번, 3이면 7번, 4면 15번 
def solution(n, start = 1, mid = 2, end = 3, answer = []):
    if n == 1:
        return [[start, end]]
    if n == 2:
        return [[start, mid], [start, end], [mid, end]]
    answer.extend(solution(n = n - 1, start = start, mid = end, end = mid, answer = []))
    answer.append([start, end])
    answer.extend(solution(n = n - 1, start = mid, mid = start, end = end, answer = []))
        
    return answer