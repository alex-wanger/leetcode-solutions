def longestConsecutive(nums):
    hashed = hash(nums)
    counter = 0
    max = 0
    for num in hashed:
        temp = num + 1
        while (temp in hashed):
            counter += 1
            temp += 1
        if (counter > max):
            max = counter
        counter = 0

    return max
