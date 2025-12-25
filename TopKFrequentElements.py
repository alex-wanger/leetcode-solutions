class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1

        solution = []

        keys = list(dic.keys())
        values = list(dic.values())

        # go through all values
        for j in range(k):
            m = max(values)
            for i in range(len(values)):
                if (values[i] == m):
                    solution.append(keys[i])
                    values[i] = 0
                    # make it zero that it is effectively removed
                    break
        return solution
