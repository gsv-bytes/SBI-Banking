print("Hi User!")
print("Welcome to SBI Bank")
print("Please select the option you want to perform:")

user_data = {}
balance = 0
total_credit = 0
total_debit = 0

while True:
    print("\n--- MAIN MENU ---")
    print("Press 1 to Register")
    print("Press 2 to Login")
    print("Press 3 to TERMINATE")
    option = input("Enter your option: ")

    if option not in ["1", "2", "3"]:
        print("Invalid option! Please try again.")
        continue

    if option == "1":
        print("\n--- REGISTRATION ---")
        age = input("Enter your AGE: ")
        while not age.isdigit() or int(age) < 18:
            print("Invalid! AGE should be a number and >= 18.")
            age = input("Enter your AGE: ")

        name = input("Enter your FIRST NAME: ")
        while not name.replace(" ", "").isalpha():
            print("Invalid! Name should contain only letters.")
            name = input("Enter your FIRST NAME: ")

        last_name = input("Enter your LAST NAME: ")
        while not last_name.replace(" ", "").isalpha():
            print("Invalid! Last name should contain only letters.")
            last_name = input("Enter your LAST NAME: ")

        phone = input("Enter your PHONE NUMBER: ")
        while not phone.isdigit() or len(phone) != 10:
            print("Invalid! Phone number should be 10 digits.")
            phone = input("Enter your PHONE NUMBER: ")

        email = input("Enter your EMAIL: ")
        while "@" not in email or ".com" not in email:
            print("Invalid! Please enter a valid email.")
            email = input("Enter your EMAIL: ")

        password = input("Enter your PASSWORD: ")
        while len(password) < 8 or not password.isalnum():
            print("Invalid! Password must be at least 8 characters and alphanumeric.")
            password = input("Enter your PASSWORD: ")

        city = input("Enter your CITY: ")
        while not city.strip():
            print("Invalid! City cannot be empty.")
            city = input("Enter your CITY: ")

        state = input("Enter your STATE: ")
        while not state.strip():
            print("Invalid! State cannot be empty.")
            state = input("Enter your STATE: ")

        country = input("Enter your COUNTRY: ")
        while not country.strip():
            print("Invalid! Country cannot be empty.")
            country = input("Enter your COUNTRY: ")

        pin = input("Enter your PIN CODE: ")
        while not pin.isdigit() or len(pin) != 6:
            print("Invalid! Pin code should be 6 digits.")
            pin = input("Enter your PIN CODE: ")
        print("")
        print("Select Account Type:")
        print("1. Saving")
        print("2. Current")
        print("3. Fixed Deposit")
        account_type = input()
        while account_type not in ["1", "2", "3"]:
            print("Invalid! Please select 1, 2, or 3.")
            account_type = input("Enter account type: ")

        account_type = "Saving" if account_type == "1" else "Current" if account_type == "2" else "Fixed Deposit"
        account_num = "432877" + phone[-4:]

        user_data = {
            "Name": f"{name} {last_name}",
            "Phone": phone,
            "Email": email,
            "Password": password,
            "City": city,
            "State": state,
            "Country": country,
            "Pin": pin,
            "Account Type": account_type,
            "Account Number": account_num,
        }

        print("\nRegistration Successful! Here are your account details:")
        for key, value in user_data.items():
            print(f"{key}: {value}")
        print("\nPlease login to your account.")
        print("Enter your password to login:")
        entered_password = input()
        while entered_password != user_data.get("Password", ""):
            print("Invalid password! Try again.")
            entered_password = input("Enter your password: ")

        print("\nLogin successful! Welcome to SBI Bank.")

        while True:
            print("\n--- SUB MENU ---")
            print("Press 1 to MENU")
            print("Press 2 to QUICK ACCESS")
            print("Press 3 to EXIT")
            sub_option = input("Enter your option: ")

            if sub_option == "1":
                while True:
                    print("\n--- BANKING MENU ---")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Check Balance")
                    print("4. Fund Transfer")
                    print("5. Exit")
                    menu_option = input("Enter your option: ")

                    if menu_option == "1":
                        amount = input("Enter deposit amount: ")
                        while not amount.isdigit() or int(amount) <= 0:
                            print("Invalid amount!")
                            amount = input("Enter deposit amount: ")
                        amount = int(amount)
                        balance += amount
                        total_credit += amount
                        print(f"Deposited: ₹{amount}")
                        with open("transaction.txt", "a") as file:
                            file.write(f"Deposited {amount} | Balance: {balance}\n")
                        continue

                    elif menu_option == "2":
                        amount = input("Enter withdrawal amount: ")
                        while not amount.isdigit() or int(amount) > balance or int(amount) <= 0:
                            print("Invalid or insufficient balance!")
                            amount = input("Enter withdrawal amount: ")
                        amount = int(amount)
                        balance -= amount
                        total_debit += amount
                        print(f"Withdrawn: ₹{amount}")
                        with open("transaction.txt", "a") as file:
                            file.write(f"Withdrawn {amount} | Balance: {balance}\n")
                        continue

                    elif menu_option == "3":
                        print(f"Current Balance: ₹{balance}")
                        with open("transaction.txt", "a") as file:
                            file.write(f"Checked Balance | Balance: {balance}\n")
                        continue

                    elif menu_option == "4":
                        transfer_account = input("Enter target account number (10 digits): ")
                        while not transfer_account.isdigit() or len(transfer_account) != 10:
                            print("Invalid account number!")
                            transfer_account = input("Enter target account number: ")
                        amount = input("Enter transfer amount: ")
                        while not amount.isdigit() or int(amount) > balance:
                            print("Invalid or insufficient balance!")
                            amount = input("Enter transfer amount: ")
                        amount = int(amount)
                        balance -= amount
                        total_debit += amount
                        print(f"Transferred: ₹{amount} to Account {transfer_account}")
                        print(f"New Balance: ₹{balance}")
                        with open("transaction.txt", "a") as file:
                            file.write(f"Transferred {amount} to Account {transfer_account} | Balance: {balance}\n")
                        continue

                    elif menu_option == "5":
                        print("Exiting banking menu.")
                        break

                    else:
                        print("Invalid option!")
                        break

            elif sub_option == "2":
                print("\n--- QUICK ACCESS ---")
                print("1. Account Statement")
                print("2. Customer Care")
                print("3. Savings Info")
                print("4. Analyze Transaction History")
                print("5. Exit")

                quick_option = input("Enter your option: ")

                if quick_option == "1":
                    print("\nAccount Statement:")
                    print(f"Account Number: {user_data['Account Number']}")
                    print(f"Total Credit: ₹{total_credit}")
                    print(f"Total Debit: ₹{total_debit}")
                    print(f"Current Balance: ₹{balance}")
                    continue

                elif quick_option == "2":
                    print("Customer Care: Call 1800-123-4567. 24/7 support available.")
                    continue

                elif quick_option == "3":
                    print("")
                    print("--- SAVINGS INFO ---")
                    print("1. Regular Savings\n2. SIP\n3. SWP\n4. Exit")
                    savings_option = input("Choose savings type: ")

                    if savings_option == "1":
                        amo = int(input("Enter amount to deposit: "))
                        time = int(input("Enter time (months): "))
                        result = (amo * time * 0.225) / 100 + amo
                        print(f"Amount after saving: ₹{result:.2f}")
                        print(f"Interest Rate: 0.225%")
                        print(f"Interest earned: ₹{result - amo:.2f}")
                        continue

                    elif savings_option == "2":
                        amo = float(input("Enter SIP amount: "))
                        time = int(input("Enter time (months): "))
                        r = 20 / (12 * 100)
                        fv = amo * (((1 + r) ** time - 1) / r) * (1 + r)
                        print(f"SIP Future Value: ₹{fv:.2f}")
                        print(f"Interest Rate: 20%")
                        print(f"Interest earned: ₹{fv - (amo * time):.2f}")
                        continue

                    elif savings_option == "3":
                        principal = float(input("Enter SWP amount: "))
                        time = int(input("Enter withdrawal duration (months): "))
                        r = 20 / (12 * 100)
                        swp = (principal * r) / (1 - (1 + r) ** -time)
                        print(f"SWP Monthly Withdrawal: ₹{swp:.2f}")
                        print(f"Interest Rate: 20%")
                        print(f"Total amount withdrawn: ₹{swp * time:.2f}")
                        print(f"Total interest earned: ₹{swp * time - principal:.2f}")
                        continue
                    elif savings_option == "4":
                        print("Exiting savings info.")
                        break
                    else:
                        print("Invalid savings option.")
                        break

                elif quick_option == "4":
                    with open("transaction.txt", "r") as file:
                        print("Transaction History:")
                        print(file.read())
                    continue
                elif quick_option == "5":
                    print("Exiting quick access.")
                    continue

                else:
                    print("Invalid option! Try again.")
                    continue
            elif sub_option == "3":
                print("Exiting the program.")
                break
            else:
                print("Invalid option! Try again.")
                break
    elif option == "2":
        print("please go to register first then i will direct you to login automatically!")
        print("Thank you for using SBI Bank. Goodbye!")
        continue

    elif option == "3":
        print("Thank you for using SBI Bank. Goodbye!")
        break
        

    else:
        print("Invalid option! Try again.")
        break
