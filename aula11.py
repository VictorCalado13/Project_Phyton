# Precedência entre os operadores aritméticos

# Passo a passo dos mais fortes

# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

#Ex: Resposta 1024

#conta_ex = 1 + 1 ** 5 + 5
#print(conta_ex) # Esta printando valor 7

# Correção 1

conta_1 = (1 + 1) ** (5 + 5)
print(conta_1)

# Correção 2

conta_2 = (1 + int(0.5 + 0.5)) ** (5 + 5) # 7
print(conta_2)