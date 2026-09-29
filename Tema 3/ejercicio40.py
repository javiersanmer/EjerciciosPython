while True:
    nums_txt = input("Introduce un num: ")

    nums = nums_txt.split(";")

    for i in range(len(nums)):
        nums[i] = int(nums[i])

    print(max(nums))
    print(min(nums))    
    print(sum(nums)/len(nums))