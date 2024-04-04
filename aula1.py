#print('Hello World!')

#utilizando separadores
#print(12,34, sep= '-')
#print(12,34, sep= '-')

# para quebra de linha \r\n
##print(12,34, sep= '\r\n')

#str -> String -> 
#Aspas simples
#print('Reinaldo')

#Aspas Duplas
#print("Reinaldo")

#Escape 
#print(r"Reinaldo \"Yungh\"")

# int
#print(11)

#float
#print(1.1)

#type - mostra o tipo que o python inferiou ao valor
#print(type('Reinaldo'))

#boolean
#print(10==10)
#print(10==11)
#print(type(10==10))

#conversao de tipos
#print(int('1')+1)

#variavel
# nome_completo = 'Reinaldo Yungh'
# soma_dos_numeros = 2+2
# print(nome_completo, soma_dos_numeros)

#concatenando impressao
# nome = 'Reinaldo'
# idade = 35
# print('Nome: ', nome, ', Idade: ', idade)

#exercicio
# nome = 'Reinaldo'
# sobrenome = 'Yungh'
# idade = 35
# ano_nascimento = 2024 - idade
# maior_de_idade = 35>=18
# altura_metros = 1.97

# print('Nome: ', nome)
# print('Sobrenome: ', sobrenome)
# print('idade: ', idade)
# print('Ano Nascimento: ', ano_nascimento)
# print('Maior de Idade: ', maior_de_idade)
# print('Altura Metros: ', altura_metros)

#calculos
# adicao = 10 + 10
# print('Adição', adicao)

# subtracao = 10 - 5
# print('Subtração', subtracao)

# multiplicacao = 10 * 10
# print('Multiplicação', multiplicacao)

# divisao = 10 / 3  # float
# print('Divisão', divisao)

# divisao_inteira = 10 // 3
# print('Divisão inteira', divisao_inteira)

# exponenciacao = 2 ** 10
# print('Exponenciação', exponenciacao)

# modulo = 55 % 2  # resto da divisão
# print('Módulo', modulo)

#concatenacao
# concatenacao = 'Luiz' + ' ' + 'Otávio'
# print(concatenacao)

# a_dez_vezes = 'A' * 10
# tres_vezes_luiz = 3 * 'Luiz'
# print(a_dez_vezes)
# print(tres_vezes_luiz)

#precedencia
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -
# conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
# print(conta_1)

#exercicio
# nome = 'Reinaldo'
# peso = 120
# altura = 1.97
# imc = peso / (altura*altura)

# if imc <= 18.5:
#     print('MAGREZA')
# elif imc > 18.5 and imc < 24.9:
#     print('NORMAL')
# elif imc > 25 and imc < 29.9:
#     print('SOBREPESO')
# elif imc > 30 and imc < 39.9:
#     print('OBESIDADE')
# elif imc > 40 :
#     print('OBESIDADE GRAVE')
# else:
#     print('Não foi possível calcular')

# f-strings
# linha_1 = f'{nome} tem {altura:.2f} de altura,'
# linha_2 = f'pesa {peso} quilos e seu imc é'
# linha_3 = f'{imc:.2f}'

# print(linha_1)
# print(linha_2)
# print(linha_3)

#inserir dados 
nome  = input('Qual o seu nome? ')
print(f'O seu nome é: {nome}')



