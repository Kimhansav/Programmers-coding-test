#E,W : w방향, S, N : h방향, 좌표 : [w][h]
def solution(park, routes):
    answer = []
    max_w, max_h = len(park[0]), len(park)
    min_w, min_h = 0, 0
    park_index = ''.join(park)
    loc = park_index.index('S')
    cur_h, cur_w = loc // max_w, loc % max_w
    for move in routes:
        info = move.split(' ')
        dist = int(info[1])
        if info[0] == 'E':
            if cur_w + dist < max_w:
                path = [park[cur_h][cur_w + i + 1] for i in range(dist)]
                if 'X' not in path:
                    cur_w += dist
        if info[0] == 'W':
            if cur_w - dist >= 0:
                path = [park[cur_h][cur_w - i-1] for i in range(dist)]
                if 'X' not in path:
                    cur_w -= dist
                
        if info[0] == 'S':
            if cur_h + dist < max_h:
                path = [park[cur_h + i + 1][cur_w] for i in range(dist)]
                if 'X' not in path:
                    cur_h += dist
        if info[0] == 'N':
            if cur_h - dist >= 0:
                path = [park[cur_h - i-1][cur_w] for i in range(dist)]
                if 'X' not in path:
                    cur_h -= dist
        
    return [cur_h, cur_w]