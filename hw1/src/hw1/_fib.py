def fib(n: int) -> int:
    assert n > 0

    nums = [0, 1]

    for i in range(n - 1):
        _next = nums[0] + nums[1]
        nums[0] = nums[1]
        nums[1] = _next

    return nums[0]
