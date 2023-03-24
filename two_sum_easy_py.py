def two_sum(nums, target):
    answer = []
    for idx, num in enumerate(nums):
        if num in answer: return [answer.index(num), idx]
        answer.append(target - num )