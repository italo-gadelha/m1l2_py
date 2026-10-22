import random

char = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
qt = int(input("Digite a quantidade de caracteres para a senha:"))
senha = ""

for i in range(qt):
    senha += random.choice(char)

print(senha)
