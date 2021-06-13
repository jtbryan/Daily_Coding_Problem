import random

limit = set(range(1, 122500))

with open ("input4.txt", "w") as f:
    nums = []
    for i in range(1, 95000):
        while True:
            num = str(random.randint(1, 202500))
            if num not in nums:
                nums.append(num)
                break
    ress = ""
    for num in nums:
        ress += num 
        ress += ", "
    ress = ress[:-2]
    f.write(ress)