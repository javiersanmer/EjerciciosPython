num = int(input("Introduce un número: "))
primo = True
for i in range(2,num):
    if num % i == 0:
        primo = False
        break

if primo == True:
    print("Es primo")
else:
    print("No es primo")
    

