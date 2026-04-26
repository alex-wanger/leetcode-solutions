def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while (left < right):
            left_number = numbers[left]
            right_number = numbers[right]

            summ = left_number + right_number
            if (summ == target):
                return [left + 1, right + 1]
            
            if (summ > target):
                right -= 1
            else:
                left += 1
        return None
