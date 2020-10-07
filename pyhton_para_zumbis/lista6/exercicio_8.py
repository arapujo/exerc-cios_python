# H. apaga
# seja uma string s e um inteiro n
# retorna uma nova string sem a posição n
# apaga('kitten', 1) -> 'ktten'
# apaga('kitten', 4) -> 'kittn'

def apaga(s, n):
    nova_string = s[:n] + s[n+1:]
    return nova_string

print(apaga('sabonete', 3))
    