valid_name = False
valid_salary = False
valid_bonus = False

# Loop to check name
while not valid_name:
    try:
        name = input("Enter your name: ")
        if len(name) == 0:
            raise ValueError("The name is empty")
        elif any(char.isdigit() for char in name):
            raise ValueError("The name should not contain numbers")
        else:
            print("Valid name", name)
            valid_name = True
    except ValueError as e:
        print(e)

# Loop to check salary
while not valid_salary:
    try:
        salary = float(input("Enter your salary amount: "))
        if salary < 0:
            print("Please enter a positive value")
        else:
            print("R$", salary)
            valid_salary = True
    except ValueError:
        print("Invalid entry for salary. Please enter a number")

# Loop to check bonus
while not valid_bonus:
    try:
        bonus_received = float(input("Enter the bonus received amount: "))
        if bonus_received < 0:
            print("Please, enter a positive value for the bonus.")
        else:
            valid_bonus = True
    except ValueError:
        print("Invalid entry for bonus. Please, enter a number.")


final_bonus = 1000 + salary * bonus_received  # Example, adjust as needed

# Prints the information to the user
print(f"{name}, your salary is R${salary:.2f} and your final bonus is R${final_bonus:.2f}.")
