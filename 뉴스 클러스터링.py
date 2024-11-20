def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    str1_dict = {}
    str2_dict = {}
    
    for i in range(len(str1) - 1):
        char = str1[i] + str1[i + 1]
        if char.isalpha():
            if char not in str1_dict:
                str1_dict[char] = 1
            else:
                str1_dict[char] += 1
                
    for i in range(len(str2) - 1):
        char = str2[i] + str2[i + 1]
        if char.isalpha():
            if char not in str2_dict:
                str2_dict[char] = 1
            else:
                str2_dict[char] += 1
    
    str1_multiset, str2_multiset = set(list(str1_dict.keys())), set(list(str2_dict.keys()))
    numer, denom = 0, 0
    
    for item in str1_multiset & str2_multiset:
        numer += min(str1_dict[item], str2_dict[item])
    for item in str1_multiset | str2_multiset:
        denom += max(str1_dict[item], str2_dict[item])
    
    
    if len(str1_multiset) == 0 and len(str2_multiset) == 0:
        return 65536
    answer = int(numer / denom * 65536)
    return answer


print(solution('FRANCE','french'))
# print(solution('aa1+aa2','AAAA12'))
# print(solution('E=M*C^2','e=m*c^2'))