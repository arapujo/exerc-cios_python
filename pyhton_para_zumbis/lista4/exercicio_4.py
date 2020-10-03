''' Seja o statement sobre diversida de: “ The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.”.
Gere uma lista de palavras deste texto com split(), a seguir crie uma lista com as palavras que começam ou terminam com uma das letras
“python”. Imprima a lista resultante. Não se esqueça de remover antes os caracteres especiais
e cuidado com maiúsculas e minúsculas '''


statement= "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you."
statement = statement.lower()
statement = statement.replace(" ," , " " )
statement = statement.split()
print(statement)

while 

string_1 = 'Print only the words that start with s in this sentence'
lista = []
lista_de_palavras = string_1.split(" ")
for palavra in lista_de_palavras:
    if "s" == palavra.lower()[0]:
        lista = palavra
        print(lista)
