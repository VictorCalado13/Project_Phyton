#Introduçõa as f-strings (formatação de strings)


nome = 'Victor Calado'
altura = 1.71
peso = 82
imc = peso / altura ** 2

"f-strings"


linha_1 = f'{nome} tem {altura:.2f} de altura,' #:.2f é o numero de casas decimais
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Victor Calado tem 1.71 de altura
# Pesa 82 quilos e seu IMC é 
# 29.320987654320987