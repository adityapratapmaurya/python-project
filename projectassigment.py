#project1
balance = 10000
attempt = 0
correct_pin = 1234

while attempt < 3:
    user_pin = int(input("Enter Your Pin: "))
    
    if user_pin == correct_pin:
        while True:
            print("1. Check Balance  2. Deposit  3. Withdraw  4. Exit")
            user_input = int(input("Enter Your Option: "))
            
            if user_input == 1:
                print(balance)
                
            elif user_input == 2:
                deposit = int(input("Enter Your Amount to deposit: "))
                balance += deposit
                print(f"Balance: {balance}")
                
            elif user_input == 3:
                withdraw = int(input("Enter Your Amount to withdraw: "))
                if withdraw <= balance:
                    balance -= withdraw
                    print(f"Remaining Amount: {balance}")
                else:
                    print("Insufficient balance")
                    
            elif user_input == 4:
                print("Thank You for Banking with Us")
                break  
            
                
        break  

    else:
        attempt += 1
        print(f"Pin invalid Attempts left: {3 - attempt}")

if attempt == 3:
    print("Card Blocked")




#project 2
students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}

while True:
    print("\n--- Student Marks Manager ---")
    print("1. Add student")
    print("2. View all")
    print("3. Show topper")
    print("4. Exit")
    
    choice = input("Enter choice (1-4): ").strip()
    
    if choice == "1":
        name = str(input("Enter student name: ")).strip()
        if name in students:
            print("Student already exists.")
        else:
            marks = []
            valid = True
            for i in range(1, 4):
                mark_str = input(f"Enter mark {i}: ").strip()
                if mark_str.replace('.', '', 1).isdigit():
                    mark = float(mark_str)
                    if 0 <= mark <= 100:
                        marks.append(mark)
                    else:
                        print("Invalid mark, try again.")
                        valid = False
                        break
                else:
                    print("Invalid mark, try again.")
                    valid = False
                    break
            
            if valid and len(marks) == 3:
                students[name] = marks

    elif choice == "2":
        for name, marks in students.items():
            avg = sum(marks) / len(marks)
            if avg >= 85:
                grade = "A"
            elif avg >= 70:
                grade = "B"
            elif avg >= 50:
                grade = "C"
            else:
                grade = "F"
            print(f"{name} {avg:.2f} {grade}")

    elif choice == "3":
        topper_name = ""
        highest_avg = 0
        for name, marks in students.items():
            avg = sum(marks) / len(marks)
            if avg >= highest_avg:
                highest_avg = avg
                topper_name = name
                
        if topper_name != "":
            print(f"Topper: {topper_name}")

    elif choice == "4":
        print("Goodbye!")
        break
    

    else:
        print("Invalid choice, please select between 1 and 4.")    