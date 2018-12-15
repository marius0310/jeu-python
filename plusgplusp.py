import random

solution = random.randint(1,1000)
essai = 0

for i in range(20):
    nombre = int(input("Quel est le nombre? "))

    if nombre==solution:
        print("gagné en "+str (essai)+" coup")
        break


    if solution<nombre:
        essai +=1
        print ("plus petit")

    if solution>nombre:
        essai +=1
        print ("plus grand")

if nombre!=solution:
    print ("perdu")
    
