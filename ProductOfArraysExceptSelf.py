def productExceptSelf(sel, nums):
    n = len(nums)

    prefix = [1] * n
    suffix = [1] * n
    product = [1] * n

    prefix[0] = 1
    for i in range(1, n):
        prefix[i] = nums[i - 1] * prefix[i-1]

    suffix[0] = 1
    for i in range(n - 2, -1, -1):
        suffix[i] = nums[i+1] * suffix[i+1]

    for i in range(0, n):
        product[i] = prefix[i] * suffix[i]

    return product

    # 3 2 3
    # so index 0 = 6
    # index 1 = 3
    # index 2 = 1
    # index 0 = 1
    # index 1  = 3
    # index 2  = 6
