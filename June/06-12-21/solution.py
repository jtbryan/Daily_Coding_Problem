import time

def main_slow(nums, n):
    start_time = time.time()
    if len(nums) == 0:
        return "Empty list"

    print("\nO(n^2) Time Complexity Method...")
    for i, num in enumerate(nums):
        for j, num2 in enumerate(nums):
            if j == i:
                continue
            if num + num2 == n:
                print(f"Took {(time.time() - start_time):.2f}")
                return True
    print(f"Took {(time.time() - start_time):.2f}")
    return False

def main_fast(nums, n):
    start_time = time.time()
    if len(nums) == 0:
        return "Empty list"

    print("\nBonus: O(n) Time Complexity Method...")
    # The set has an 0(1) lookup
    checkset = set()
    for i, num in enumerate(nums):
        if (n - num) in checkset:
            print(f"Took {(time.time() - start_time):.2f}")
            return True
        if num not in checkset:
            checkset.add(num)    

    print(f"Took {(time.time() - start_time):.2f}")
    return False

if __name__ == "__main__":
    with open("./input4.txt") as f:
        nums = f.readline().split(",")
        nums = [int(i) for i in nums]
        n = int(f.readline())
        expected_res = f.readline()
        if expected_res == "True":
            expected_res = True
        else:
            expected_res = False
    print(f"Expected result: {expected_res}")
    
    res1 = main_slow(nums, n)
    res2 = main_fast(nums, n)

    try:
        assert res1 == expected_res
        print(f"\nExpected result achieved, got {res1}")
    except AssertionError:
        print(f"\nExpected result not achieved, instead got {res1}")

    try:
        assert res2 == expected_res
        print(f"\nExpected result achieved, got {res2}")
    except AssertionError:
        print(f"\nExpected result not achieved, instead got {res2}")