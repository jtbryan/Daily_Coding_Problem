def main_with_division(nums):
    '''
    This method involves the use of division. If we evaluate the product of an entire list of numbers, we will have: product = a*b*c. Using this, we can evaluate the result at i by dividing the index we are currently at. This results in the following: product = (a*b*c)/a = b*c.

    Time complexity: O(n+n) = O(n)
    '''
    if len(nums) == 1 or len(nums) == 0:
        return 0

    print("\nUsing division...")

    res = []
    product = 0
    for i in range(1, len(nums)):
        if product == 0:
            product = (nums[i-1] * nums[i])
        else:
            product = (product * nums[i])

    for i, num in enumerate(nums):
        res.append(int(product/num))
    return res

def main_without_division(nums):
    '''
    Time complexity: O(n^2)
    '''
    if len(nums) == 1 or len(nums) == 0:
        return 0

    print("\nWithout division...")

    res = []
    for i in range(len(nums)):
        product = 1
        for j in range(len(nums)):
            if j != i:
                product = product * nums[j]
        res.append(product)

    return res


if __name__ == "__main__":
    with open("./input.txt") as f:
        nums = f.readline().split(",")
        nums = [int(i) for i in nums]
        expected_res = f.readline().split(",")
        expected_res = [int(i) for i in expected_res]
    print(f"Expected result: {expected_res}")

    res1 = main_with_division(nums)

    try:
        assert res1 == expected_res
        print(f"\nExpected result achieved, got {res1}")
    except AssertionError:
        print(f"\nExpected result not achieved, instead got {res1}")


    res2 = main_without_division(nums)

    try:
        assert res2 == expected_res
        print(f"\nExpected result achieved, got {res2}")
    except AssertionError:
        print(f"\nExpected result not achieved, instead got {res2}")