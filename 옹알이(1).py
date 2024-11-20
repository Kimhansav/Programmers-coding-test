def solution(babbling):
    answer = 0
    list = ["aya", "ye", "woo", "ma"]
    for babble in babbling:
        string = ""
        for i in range(len(babble)):
            string += babble[i]
            if string in list:
                string = ""
        if len(string) == 0:
            answer += 1            
            
    return answer