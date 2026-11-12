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
    print(f"{name}! you are junior-Developer ")


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
    