# Exercícios by Nick Parlante (CodingBat)

# A. multstring
# seja uma string s e um inteiro positivo n
# retorna uma string com n cópias da string original
# multstring('Hi', 2) -> 'HiHi'
def multstring(s, n):
    if s and n >= 0:
        return print(s*n)

multstring('Hi', 2)

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