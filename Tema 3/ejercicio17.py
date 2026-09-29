suma = 0
nums = []
while True:
    num = int(input("Introduce números: "))
    if num == 0:
        break
    
    nums.append(num)
    suma+= num

media = num / len(nums)
    
for num in nums:
    if num > media:
        print(f"{num} es mayor que la media")
