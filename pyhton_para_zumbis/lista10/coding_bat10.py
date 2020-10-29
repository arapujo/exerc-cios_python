# Exercícios by Nick Parlante (CodingBat)

# A. near_ten #
# Seja um n não negativo, retorna True se o número está a distância de
# pelo menos dois de um múltiplo de dez. Use a função resto da divisão.
# near_ten(12) -> True
# near_ten(17) -> False
# near_ten(19) -> True

def near_ten(n):
    dist = n % 10

    if dist <= 2 or dist >= 8:
        return True
    return False

# B. lone_sum
# Soma maluca: some os números inteiros a, b, e c
# Se algum número aparecer repetido ele não conta na soma
# lone_sum(1, 2, 3) -> 6
# lone_sum(3, 2, 3) -> 2
# lone_sum(3, 3, 3) -> 0

def lone_sum(a, b, c):
    if a != b and a != c:
        return a + b + c
    elif a == b and a == c:
        return 0
    elif b == a:
        return c
    elif a == c:
        return b
    elif b == c:
        return a

# C. luck_sum #
# Soma três inteiros a, b, c
# Se aparecer um 13 ele não conta e todos os da sua direita também
# lucky_sum(1, 2, 3) -> 6
# lucky_sum(1, 2, 13) -> 3
# lucky_sum(1, 13, 3) -> 1

def lucky_sum(a, b, c):
  if a == 13:
    return 0
  elif b == 13:
    return a
  elif c == 13:
    return a + b
  elif  a != b and a != c:
    return a + b + c

# D. double_char #
# retorna os caracteres da string original duplicados
# double_char('The') -> 'TThhee'
# double_char('AAbb') -> 'AAAAbbbb'
# double_char('Hi-There') -> 'HHii--TThheerree'

def double_char(s):
	duplicada = ''
	for letra in s:
		duplicada += letra * 2
	return duplicada

# E. count_hi #
# conta o número de vezes que aparece a string 'hi'
# count_hi('abc hi ho') -> 1
# count_hi('ABChi hi') -> 2
# count_hi('hihi') -> 2

def count_hi(s):
  quantidade = s.count('hi')
  return quantidade

# F. cat_dog #
# verifica se o aparece o mesmo número de vezes 'cat' e 'dog'
# cat_dog('catdog') -> True
# cat_dog('catcat') -> False
# cat_dog('1cat1cadodog') -> True

def cat_dog(s):
  qtd_cat = s.count('cat')
  qtd_dog = s.count('dog')
  return qtd_cat == qtd_dog

# G. count_code #
# conta quantas vezes aparece 'code'
# a letra 'd' pode ser trocada por outra qualquer
# assim 'coxe' ou 'coze' também são contadas como 'code'
# count_code('aaacodebbb') -> 1
# count_code('codexxcode') -> 2
# count_code('cozexxcope') -> 2

def count_code(s):
  contador = 0
  for i in range(len(s)-3):
    if s[i:i+2] == 'co' and s[i+3] == 'e':
      contador += 1
  return contador
 

# H. end_other #
# as duas strings devem ser convertidas para minúsculo via lower()
# depois disso verifique que no final da string b ocorre a string a
# ou se no final da string a ocorre a string b
# end_other('Hiabc', 'abc') -> True
# end_other('AbC', 'HiaBc') -> True
# end_other('abc', 'abXabc') -> True

def end_other(a, b):
  a = a.lower()
  b = b .lower()
  tamanho = len(a) - len(b)
  
  if a[abs(tamanho):] == b or b[abs(tamanho):] == a:
    return True
  return False

# I. count_evens
# conta os números pares da lista
# count_evens([2, 1, 2, 3, 4]) -> 3
# count_evens([2, 2, 0]) -> 3
# count_evens([1, 3, 5]) -> 0

def count_evens(nums):
  contador = 0
  for i in nums:
    if i % 2 == 0:
      contador += 1
  return contador  
 
# J. sum13 #
# retorna a soma dos números de uma lista
# 13 dá azar, você deverá ignorar o 13 e todos os números à sua direita
# sum13([1, 2, 2, 1]) -> 6
# sum13([1, 1]) -> 2
# sum13([1, 2, 2, 1, 13]) -> 6
# sum13([13, 1, 2, 3, 4]) -> 0

def sum13(nums):
  if 13 in nums:
    return sum(nums[:nums.index(13)])
  return sum(nums)

# K. has22 #
# Verifica se na lista de números inteiros aparecem dois 2 consecutivos
# has22([1, 2, 2]) -> True
# has22([1, 2, 1, 2]) -> False
# has22([2, 1, 2]) -> False

def has22(nums):
	lista = []
	for i in range(0, len(nums)):
		if nums[i] == 2:
			lista.append(i)
	for i in range(0, len(lista)-1):
		if lista[i+1] - lista[i] == 1:
			return True
	return False

# L. soma_na_lista #
# Verifica se um número é soma de dois elementos distintos de uma lista
# soma_na_lista(5, [1, 2, 3, 4]) -> True
# soma_na_lista(9, [1, 2, 3, 4]) -> False
# soma_na_lista(0, [1, 2, 3, 4]) -> False
# soma_na_lista(8, [1, 2, 3, 4]) -> False
# soma_na_lista(4, [2, 2, 2, 2]) -> False
# soma_na_lista(4, [2, 2, 1, 3]) -> True

def soma_na_lista(n, lista):
	for j in range(len(lista)):
		for k in range(len(lista)):
			if j != k and lista[j] != lista[k] and lista[j] + lista[k] == n:
				return True
	return False

# M.Difícil: Fila de tijolos sem usar loops #
# queremos montar uma fila de tijolos de um tamanho denominado meta
# temos tijolos pequenos (tamanho 1) e tijolos grandes (tamanho 5)
# retorna True se for possível montar a fila de tijolos
# é possível uma solução sem usar for ou while
# fila_tijolos(3, 1, 8) -> True
# fila_tijolos(3, 1, 9) -> False
# fila_tijolos(3, 2, 10) -> True

def fila_tijolos(n_peq, n_gra, meta):
   return n_peq >= meta % 5 and n_peq + 5 * n_gra >= meta
  