nums = []
i= 0
while True:
    n = int(input("Introduce un número: "))

    if n > 0:
        nums.append(n)
    else:
        nums.remove(n*(-1))
    
    print(nums)
