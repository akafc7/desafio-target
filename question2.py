# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

def count_letter_a(input_string):
    lowercase_string = input_string.lower()
    count = lowercase_string.count('a')
    
    return count

user_input = input("Digite uma frase ou palavra: ")
result = count_letter_a(user_input)

if result > 0:
    print(f"A letra 'a' aparece {result} vezes na string.")
else:
    print("A letra 'a' não foi encontrada na string.")
