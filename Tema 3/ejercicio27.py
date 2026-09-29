import random
nums = []
for _ in range(1000):
    nums.append(random.randint(1, 100))

masRepetido = nums[0]

for n in nums:
    if nums.count(n) > nums.count(masRepetido):
        masRepetido = n

print(f"El más repetido es: {n} y se repite {nums.count(n)}")
