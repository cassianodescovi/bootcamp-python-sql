# Requests the user to type their name
try:
    name = input("Enter your name: ")
    # Checks if the name is empty
    if len(name) == 0:
        raise ValueError("The name is empty")
    elif any(char.isdigit() for char in name):
        raise ValueError("The name should not contain numbers")
    else:
        print("Valid name", name)
except ValueError as e:
    print(e)

# Requests the user to enter their salary amount and converts it to float
try:
    salary = float(input("Enter your salary amount: "))
    if salary < 0:
        print("Please enter a positive value")
    else:
        print("R$", salary)
except ValueError:
    print("Invalid entry for salary. Please enter a number")

# Requests the user to enter the bonus received amount and converts it to float
try:
    bonus_received = float(input("Enter the bonus received amount: "))
    if bonus_received < 0:
        print("Please, enter a positive value for the bonus.")
except ValueError:
    print("Invalid entry for bonus. Please, enter a number.")

# Assuming a calculation logic for the final bonus and KPI
final_bonus = bonus_received * 1.2  # Example, adjust as needed
kpi = (salary + final_bonus) / 1000  # Simple KPI example

# Prints the information to the user
print(f"Your KPI is: {kpi:.2f}")
print(f"{name}, your salary is R${salary:.2f} and your final bonus is R${final_bonus:.2f}.")
