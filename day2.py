print("  ---- Day-2: Jobe Eligibility Checkwer -----")
# print(f"Candidate name is: {name}")
# print(f"{name} has {Experience} years of experience")
name = input("Enter your full name: ")
Experience = int(input("Enter Your Experience: "))
knows_python = input("Do you know python: ").lower().strip()
knows_DOTNET  = input("Do you Know DOTNET: ").lower().strip()


if Experience >=5 and  (knows_python == "yes" or knows_DOTNET == "yes" ):

    print(f"Congratulations! {name} you are eligible ")
else:
    print(f"{name}! You are not eligible.")


if Experience >= 6 :
    print(f"{name} you are a Senior-developer!")
elif Experience  >=3 :
    print(f"{name} you are a Mid-level developer !")
else:
    print(f"{name}! you are junior-Developer \n")


# if Experience >= 4:
#     print(f"{name} As yo have {Experience} years of experience , you are eligible.")
# else :
#     print(f"{name} As yo have {Experience} years of experience , you not are eligible.")

# if Experience >= 6 :
#     print(f"{name}! you are a Senior Developer ")
# elif Experience >= 3 :
#     print(f"{name}! you are mid-level devoloper ")
# else :
#     print(f"{name}! you are junior devoloper ")



print("   ---- Day-2 beginner coding challenge ----")
number = int(input("Enter a Integer: "))

if number > 0:
    print(f"{number} is a positive number.\n")

elif number < 0:
    print(f"{number} is a negative number.\n")

else:
    print(f"{number} is zero.\n")


print("   ---- Day-2 User log in ----")

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == "Laxman" and password == "Laxman@1234":
    print("you are successfully logged in!")

elif  username == "Laxman" and not password =="Laxman@1234":
    print("Incorrect Password")
else:
    print("Incorrect Username")


print("   ---- Day-2 Loan Approaval ----")

name = input("Enter your Full Name: ")
age = int(input("Enter your age: "))
salary = int(input("Enter your Monthly Salary $: "))
credit_score = int(input("Enter your cibil score: "))
loan = input("you have an excisting loan(Yes/No): ").lower()

if age >= 21 and salary >= 3000 and credit_score >= 700 and loan == "no":
    print(f"congratulations! {name} , you are eligible to get a loan.")
else:
    print(f"Sorry! {name} , you are not eligible to get a loan.")