#C. soma_dobro
# dados dois números inteiros retorna sua soma
# porém se os números forem iguais retorna o dobro da soma
# soma_dobro(1, 2) -> 3
# soma_dobro(2, 2) -> 8

def soma_dobro(a, b):
    if a==b:
        soma = (a+b) * 2
        return soma
    else:
        soma = (a+b)
        return soma

print(soma_dobro(1, 2))
print(soma_dobro(2, 2))

    

 