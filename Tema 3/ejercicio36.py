nums = []
while True:
    num = int(input("Inserta números: "))

    if num == 0:
        break
    
    nums.append(num)

nums.reverse()
n = int(input("Introduce un número n: "))

print(f"Los {n} últimos son: ")
for i in range(n):
    print(nums[i])
