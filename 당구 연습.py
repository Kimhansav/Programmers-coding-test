#쿠션을 맞춰야 하면 무조건 1쿠션이 최단 거리.
def solution(m, n, startX, startY, balls):
    answer = []
    for pos in balls:
        dist_list = []
        #대칭 4가지
        #일직선일 때 제외
        dist_list.append((startX + pos[0]) ** 2 + (startY - pos[1]) ** 2) if startY != pos[1] or startX < pos[0] else None
        dist_list.append((startX - pos[0]) ** 2 + (startY + pos[1]) ** 2) if startX != pos[0] or startY < pos[1] else None
        dist_list.append((startX - 2 * m + pos[0]) ** 2 + (startY - pos[1]) ** 2) if startY != pos[1] or startX > pos[0] else None
        dist_list.append((startX - pos[0]) ** 2 + (startY - 2 * n + pos[1]) ** 2) if startX != pos[0] or startY > pos[1] else None
        answer.append(min(dist_list))
    return answer


def dist(start_pos, end_pos):
    return (start_pos[0] - end_pos[0]) ** 2 + (start_pos[1] - end_pos[1]) ** 2
    