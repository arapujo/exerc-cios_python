''' Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” e 
que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais.
'''

statement = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."
statement = statement.lower()
statement = statement.replace(" ," , " " )
lista = statement.split()
palavra = []


for letra in lista:
    if letra[0]  in 'python': 
        palavra.append(letra)
print(palavra)
print(len(palavra))

palavra2 = []

for letra in palavra:
    if len(letra) > 4:
        palavra2.append(letra)
print(palavra2)
print(len(palavra2))