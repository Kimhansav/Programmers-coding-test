def solution(players, callings):
    answer = []
    players_dict = {name : index for index, name in enumerate(players)}
    for name in callings:
        index = players_dict[name]
        catched_name = players[index - 1]
        players[index] = catched_name
        players[index - 1] = name
        players_dict[catched_name] += 1
        players_dict[name] -= 1
    return players