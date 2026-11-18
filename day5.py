# print(" ---- Lists in python without loops ----")

# balances = [5000 ,8000, 12000, 15000]

# print(balances[0])
# print(balances[1])
# print(balances[2])
# print(balances[3])


# print(" ---- Examples of Append , remove , length od List ----")

# balances = [5000, 6000, 7000]
# balances.append(8000)
# balances.remove(6000)
# print(balances)
# print(len(balances))

# print(" ---- Examples of Lists ----")

# balances = [ 5000, 8000, 12000, 15000]
# print (f"balnce of Ac holders: {balances}")
# balances[1] = balances[1]+2000
# print (f"balance of Ac holdres after adding 2000: {balances}")

# print(" ---- combinig lists with loop ----")
# balances = [ 5000, 8000, 12000, 15000]

# for balance in balances :
#     print(balance)


# print("---- printing indexes with loops ----")
# balances = [ 5000, 8000, 12000, 15000]
# for i in range(len(balances)):
#     print(i , balances[i])

# print("---- printing total-balances with loops ----")
# balances = [ 5000, 8000, 12000, 15000]
# total = 0
# for balance in balances :
#     total = total + balance
# print(f"Total Ac balances are: {total}")
# print(" ---- list operations ----")
# balances = [5000, 8000, 12000, 15000]
# print(balances[0])
# print(balances[2])

# balances[1] = balances[1] + 2000
# print(balances[1])

# balances[3] = balances[3] - 3000
# print(balances[3])

# print(balances)

# print("---- list operations using methods of list")
# customers = ["Rahul", "Sai", "Arjun", "Ravi"]
# print(customers)
# customers.append("Kiran")
# customers.remove("Sai")
# print(len(customers))
# print(customers)

# print(" ---- Examples of lists")
# balances = [3000, 8500, 12000, 4500, 15000]
# count = 0
# total = 0

# print(f"ac balances:")
# for balance in balances:
#     print(balance)

# print(f"ac balances above 5000:")
# for balance in balances :
#     if balance > 5000 :
#         print(balance)



# for balance in balances :
#     if balance > 5000 :
#         count = count + 1
#         total = total + balance
# print(f"no of ac balances above 5000: {count}")
# print(f"total ac balances above 5000: {total}")



customers = ["Rahul", "Sai", "Arjun"]
balances = [5000, 8000, 12000]


def view_accounts(customers, balances):
    for i in range(len(customers)):
        print(f"{i + 1}. {customers[i]} - ${balances[i]}")


def check_balance(customers, balances):
    try:
        ac_number = int(input("Enter your Ac Number: "))
        index = ac_number - 1

        if 0 <= index < len(customers):
            print(f"Name of the customer: {customers[index]}")
            print(f"Ac Bal: ${balances[index]}")
        else:
            print("Invalid Account number")

    except ValueError:
        print("Please enter a valid account number")


def deposit(customers, balances):
    try:
        ac_number = int(input("Enter your Ac Number: "))
        index = ac_number - 1

        if 0 <= index < len(customers):
            amount = float(input("Enter the amount to be deposited: "))

            if 0 < amount < float("inf"):
                balances[index] = balances[index] + amount
                print(f"Customer Name: {customers[index]}")
                print(f"Deposit successful: ${amount}")
                print(f"Updated balance: ${balances[index]}")
            else:
                print("Please enter a valid positive amount")
        else:
            print("Invalid account number!")

    except ValueError:
        print("Please enter valid numeric input")


def withdraw(customers, balances):
    try:
        ac_number = int(input("Enter your Ac Number: "))
        index = ac_number - 1

        if 0 <= index < len(customers):
            amount = float(input("Enter the amount to be withdrawn: "))

            if not (0 < amount < float("inf")):
                print("Please enter a valid positive amount")

            elif amount > balances[index]:
                print("Insufficient funds")

            else:
                balances[index] = balances[index] - amount
                print(f"Customer Name: {customers[index]}")
                print(f"Withdrawal successful: ${amount}")
                print(f"Updated balance: ${balances[index]}")
        else:
            print("Invalid account number!")

    except ValueError:
        print("Please enter valid numeric input")


while True:
    print("\n===== ATM BANKING SYSTEM =====")
    print("1. View All Accounts")
    print("2. Check Account Balance")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_accounts(customers, balances)

    elif choice == "2":
        check_balance(customers, balances)

    elif choice == "3":
        deposit(customers, balances)

    elif choice == "4":
        withdraw(customers, balances)

    elif choice == "5":
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid choice. Please try again.")
