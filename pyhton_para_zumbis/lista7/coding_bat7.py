# Exercícios by Nick Parlante (CodingBat)

# A. multstring
# seja uma string s e um inteiro positivo n
# retorna uma string com n cópias da string original
# multstring('Hi', 2) -> 'HiHi'

def multstring(s, n):
    if s and n >= 0:
        return print(s*n)

# B. string_splosion
# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'

def string_splosion(s):
    string = ''
    for i in range(len(s)):
        string += s[:i+1]
    return string

print(string_splosion('Code'))
print(string_splosion('abc'))

# C. array_count9
# conta quantas vezes aparece o 9 numa lista nums

def array_count9(nums):
  return nums.count(9)

print(array_count9([1, 2, 3, 9, 9]))

# D. array_front9
# verifica se pelo menos um dos quatro primeiros é nove
# array_front9([1, 2, 9, 3, 4]) -> True
# array_front9([1, 2, 3, 4, 9]) -> False
# array_front9([1, 2, 3, 4, 5]) -> False

def array_front9(nums):
  if nums[0:5].count(9) != 0:
    return True
  else:
    return False
print(array_front9([1, 2, 3, 9, 9]))
print(array_front9([8, 7, 6, 5]))

# E. hello_name
# seja uma string name
# hello_name('Bob') -> 'Hello Bob!'
# hello_name('Alice') -> 'Hello Alice!'
# hello_name('X') -> 'Hello X!'

def hello_name(name):
  return print(f'Hello {name}')

hello_name('Bob')

# F. make_tags
# make_tags('i', 'Yay'), '<i>Yay</i>'
# make_tags('i', 'Hello'), '<i>Hello</i>'
# make_tags('cite', 'Yay'), '<cite>Yay</cite>'

def make_tags(tab, word):
  return print(f'<{tab}>{word}<{tab}>')

make_tags('i', 'Yay')
make_tags('cite', 'Yay')

# G. extra_end
# seja um string s com no mínimo duas letras
# retorna três vezes as duas últimas letras
# extra_end('Hello'), 'lololo'
# extra_end('ab'), 'ababab'
# extra_end('Hi'), 'HiHiHi'  

def extra_end(s):
  if len(s) >= 2:
    lista = list(str(s))
    t = len(lista)
    lista = lista[t - 2] + lista[-1]
    return print(lista*3)
  else:
    return print('String muito curta')

extra_end('Hello')
extra_end('ab')

# H. first_half
# seja uma string s
# retorna a primeira metade da string
# first_half('WooHoo') -> 'Woo'
# first_half('HelloThere') -> 'Hello'
# first_half('abcdef') -> 'abc'

def first_half(s):
  return s[:len(s)//2]
  
print(first_half('abcdef'))

# I. sem_pontas
# seja uma string s de pelo menos dois caracteres
# retorna uma string sem o primeiro e último caracter
# without_end('Hello') -> 'ell'
# without_end('python') -> 'ytho'
# without_end('coding') -> 'odin'

def sem_pontas(s):
    return s[1:-1]

print(sem_pontas('Hello'))

# J. roda2
# rodar uma string s duas posições
# a string possui pelo menos 2 caracteres
# left2('Hello') -> 'lloHe'
# left2('Hi') -> 'Hi'

def roda2(s):
  return s[2:] + s[:2]

print(roda2('Hello'))