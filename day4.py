print(" ---- Examples of Functions ----")

def welcome_user() :
    print("Welcome to Day 4 of Python!\nToday we are learning functions.\n Har Har Mahadev!")

    
welcome_user()
welcome_user()


print("---- Bank application ----")

def account_balance(balance , deposit):
    new_balance = balance + deposit
    print (f"Account balance: {new_balance} ")

account_balance(5000 , 2000)


print(" ---- calculating the salary ----")
name = "Laxman"
def calculate_salary(hourly_rate , hours_wordked):
    salary = hourly_rate * hours_wordked
    return salary

total_salary = calculate_salary(50 , 40)

print(f"Total Credited Salary of {name} is : {total_salary}")


print(" ---- Python Calculator ----")
def add(a,b):
    addition = a+b
    return addition
adding_two = add(20,10)

def sub(a,b):
    subtraction = a-b
    return subtraction
subtracting_two = sub(20,10)

def mul(a,b):
    multiplication = a*b
    return multiplication
multipyling_two = mul(20,10)

def div(a,b):
    if b == 0 :
        return "can not devide by zero"
    division = a/b
    return division
dividing_two = div(20,10)
dividing_two_with_zero = div(20,0)

print(f"Addition of two numbers: {adding_two} ")
print(f"Subtraction of two numbers: {subtracting_two}")
print(f"Muliplication of two numbers: {multipyling_two}")
print(f"Division of two numbers: {dividing_two}")
print(f"Division of two numbers: {dividing_two_with_zero}")


print(" ---- Interactive Calculaor ----")

def add(number1 , number2):
    addition = number1 + number2
    return addition

def sub(number1 , number2):
    subtraction = number1 - number2
    return subtraction

def mul(number1 , number2):
    multiplication = number1 * number2
    return multiplication

def div(number1 , number2):
    division = number1 / number2
    return division

number1 = float(input("Enter your first Number: "))
number2 = float(input("Enter your first Number: "))

print(f"Addition of two numbers{add(number1,number2)}")
print(f"Subtraction of two numbers{sub(number1,number2)}")
print(f"Multiplication of two numbers{mul(number1,number2)}")
print(f"Division of two numbers{div(number1,number2)}")

print(" ---- Interactive Calculaor ----")
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
try:

 number1 = float(input("Enter your first number: "))
 number2 = float(input("Enter your second number: "))

 operation = input("Select an operation (+, -, *, /): ")

 if operation == "+":
    result = add(number1, number2)

 elif operation == "-":
    result = sub(number1, number2)

 elif operation == "*":
    result = mul(number1, number2)

 elif operation == "/":
    result = div(number1, number2)

 else:
    result = "Invalid operation"
 

 print(f"Result: {result}")

except ValueError:
   print("Invalid in put! please enyter valid number ")



print("\n---- BANK APPLICATION ----")
def deposit (current_bal , amount):
    if amount < 0 :
        return "Invalid amount! Please enter a valid amount"
    else:
        balance_after_deposit = current_bal + amount
        return balance_after_deposit
def withdrawl (current_bal , amount):
    if amount <0 :
        return "Invalid amount! please enter a valid amount"
    elif amount > current_bal:
        return "insuffiecient"
    else:
        balance_after_withdrawl = current_bal - amount
        return balance_after_withdrawl

current_bal = 5000
while True:
    
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input ("Please enter your rquest number: ")

    if choice == "1":
       print("You have selected Deposit!")
       try:
           Amount = float(input("Enter amount to be Deposited:"))
       except ValueError:
           print("Enter correct amount!")
           continue 
       result = deposit(current_bal , Amount)
       if isinstance(result,(int,float)):
           current_bal = result
           print(f"Available bal: {current_bal}")
       else:
           print(result)

    elif choice == "2":
       print("You have selected withdraw!")
       try:
           Amount = float(input("Enter amount to be Withrawn:"))
       except ValueError:
           print("Enter correct amount!")
           continue 
       result = withdrawl(current_bal , Amount)
       if isinstance(result,(int,float)):
           current_bal = result
           print(f"Current balance: {current_bal}")
       else:
           print(result)
    elif choice == "3":
       print(f"You have selected Check balance! \nAvailable balace: {current_bal}")

    elif choice == "4":
       print("You have selected Exit! \nThanks for banking with us")
       break
    else:
       print("Inlvalid choice!Please select listed choices")









