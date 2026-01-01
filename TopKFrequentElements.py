

def topKFrequent(nums: List[int], k: int) -> List[int]:
    # Count frequencies
    dic = defaultdict(int)
    for i in nums:
        dic[i] += 1

    solution = []

    keys = list(dic.keys())
    values = list(dic.values())

    # go through all values
    for j in range(k):

        for i in range(len(values)):
            if (values[i] == max(values)):
                solution.append(keys[i])
                values[i] = 0
                # make it zero that it is effectively removed
                break
    print(solution)


topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2)
