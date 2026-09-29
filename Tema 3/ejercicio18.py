a = int(input("Introduce a: "))
b = int(input("Introduce b: "))

par = []
if a % 2 == 1:
    a +=1
if a % 2 == 1:
    b+=1
for nums in range(a,b,2):
    par.append(nums)
print(par)