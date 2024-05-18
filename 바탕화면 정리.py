#wallpaper를 참조할 때 wallpaper[x][y]로 참조, 이때 x는 세로 좌표, y는 가로 좌표
#최상단 줄의 파일, 제일 왼쪽&오른쪽에 있는 파일, 최하단 줄의 파일 찾기 
def solution(wallpaper):
    x_len, y_len = len(wallpaper), len(wallpaper[0])
    x_vals, y_vals = [], []
    for idx, s in enumerate(wallpaper):
        if '#' in s:
            x_val, y_val, y_rev_val = idx + 0.5, s.index('#') + 0.5, y_len - s[::-1].index('#') - 0.5
            x_vals.append(x_val)
            y_vals.extend([y_val, y_rev_val])
    min_x, min_y, max_x, max_y = min(x_vals) - 0.5, min(y_vals) - 0.5, max(x_vals) + 0.5, max(y_vals) + 0.5
    return [min_x, min_y, max_x, max_y]