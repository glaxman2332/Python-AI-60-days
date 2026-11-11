name = "Laxman"
age = 25
job_title = "Software Engineer"
experience = 4.5
is_developer = True

print("        ----- Assessmet 1 -----")
print(f"My name is{name} , I am {age} years old and I work as a {job_title}\n")

print("        ----- using f" "string -----")
print("Developer Profile  ")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Experience: {experience}")
print(f"Is He/She adeveloper:  {is_developer}\n")


print("         ----- using print statement ------")
print("Developer Profile  ")
print("Name: " , name)
print("Age:" , age)
print("Experience:" ,experience)
print("Is He/she is a developer:\n" ,is_developer)

print("         ---- Date types of variables ----")
print("Type of variable Name :" ,type (name))
print("Type of variable Age :" ,type (age))
print("Type of variable Experience :" ,type (experience))
print("Type of variable Is a developer :\n" ,type (is_developer))


print("      -----Assessemt 2-----")
hourly_rate = 50
hours_per_week = 40
print(f"Hourly Rate: ${hourly_rate}") 
print(f"Hours Per Week: {hours_per_week}\n")

weekly_salry = hourly_rate * hours_per_week 
print(f"Weekly salary : ${weekly_salry}\n")

Annual_salary = weekly_salry * 52
print(f"Laxman's Annual salary would be ${Annual_salary}\n")

Monthly_salary = Annual_salary / 12
print(f"Laxman's Montly salary would be ${Monthly_salary:.2f}\n")


print("      -----Assessemt 3-----")
name = input("Enter Name:")
print(f"Hello {name}\n")
age =int(input(f"Enter Your age {name}: "))
print(type(age))

Future_age = int(age + 5)
print(f"{name}'s age after 5 years: {Future_age}")

past_age = int(age -10)
print(f"{name}'s age 10 years ago: {past_age}")





