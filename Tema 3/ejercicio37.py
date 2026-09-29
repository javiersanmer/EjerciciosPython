import statistics
nums = []

while True:
    n = int(input("Inserta números: "))
    
    if n == 0:
        break
    else:
        nums.append(n)
 
print(f"El número máximo es {max(nums)}")
print(f"El número mínimo es {min(nums)}")
print(f"La media es {statistics.mean(nums)}") # o usamos sum(nums)/len(nums)
