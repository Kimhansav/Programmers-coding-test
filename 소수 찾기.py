def solution(n):
    answer = 0
    nums = {i + 1 for i in range(1,n)}
    for a in range(2, n):
        for i in range(1, int(n / a)):
            nums.discard(a * (i + 1))
    return len(nums)