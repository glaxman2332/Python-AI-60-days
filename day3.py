print("---- For Loop ----")
for number in range(1, 11):
    print (number)

print("---- Multiples of 5 ----")
print ("Multiples of 5 are: ")
for numbers in range(5 ,31 , 5):
    print (numbers)

print (" ---- Example for while loop with Break ----")
correct_password = "Python123"
attempt = 1

while attempt <= 3:
    entered_password = input("Enter password: ")

    if entered_password == correct_password :
        print("you have successfully logged in!")

        break
    print("Please Enter correct password!")
    attempt += 1

else:
    print("Account locked!")


print(" ---- Example for Continue ")

for number in range(1 , 11):
     if number == 5 or number == 8:
          continue
     print(number)


print ("---- nested loop example ----")
for i in range (1,4):
    for j in range (1,4):
        multiplication = i * j
        print (f"{i} * {j} =  {multiplication}")

print (" ---- nested loop with  if ---- ")
count = 0
for i in range (1,4):
    for j in range (1,4):
        multiplication = i * j
        if multiplication % 2 == 0:
         print (f"{i} * {j} =  {multiplication}")
         count += 1 
print(f"number of even count is {count} ")


print (" ---- Adding numbers using loop  ---- ")

total = 0
for number in range (1,11):
    print (number )

    total += number
   
print (f"sum of numbers 1 to 10 : {total}")

print(" ---- finding the max number ----")

transactions = [120, 450, 80, 900, 300]
largest_trans =transactions [0]

for amount in transactions:
    if amount > largest_trans :
        largest_trans = amount

print(f"Largest number amoung the trasactions: {largest_trans}  ")

print(" ---- finding the Min number ----")

transactions = [120, 450, 80, 900, 300]
largest_trans =transactions [0]

for amount in transactions:
    if amount < largest_trans :
        largest_trans = amount

print(f"Smallest number amoung the trasactions: {largest_trans}  ")



