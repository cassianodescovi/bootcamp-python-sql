CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
user_name = input("Digite o seu nome: ")

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
salary = float(input("Digite seu salário: "))

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
user_bonus = float(input("Digite o bonus: "))

# 4) Calcule o valor do bônus final
result = CONSTANTE_BONUS + salary * user_bonus

# ) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"O usuario {user_name} possui bonus de R$ {result} ")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?