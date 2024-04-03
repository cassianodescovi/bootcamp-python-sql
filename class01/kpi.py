BONUS_CONSTANT = 1000

# 1) Asks the user to type their name
user_name = input("Enter your name: ")

# 2) Asks the user to type the amount of their salary
# Converts the input to a floating-point number
salary = float(input("Enter your salary: "))

# 3) Asks the user to type the amount of the bonus received
# Converts the input to a floating-point number
user_bonus = float(input("Enter the bonus: "))

# 4) Calculate the final bonus amount
result = BONUS_CONSTANT + salary * user_bonus

# 5) Prints a customized message including the user's name, salary, and bonus
print(f"The user {user_name} has a bonus of R$ {result} ")

# Bonus: How many bugs and risks can you identify in this program?
