# Exercícios by Nick Parlante (CodingBat)

# A. first_last6
# verifica se 6 é o primeiro ou último elemento da lista nums
# first_last6([1, 2, 6]) -> True
# first_last6([6, 1, 2, 3]) -> True
# first_last6([3, 2, 1]) -> False

def first_last6(nums): #
    if nums[-1] == 6 or nums[0] == 6:
        return True
    else:
        return False

# B. same_first_last #
# retorna True se a lista nums possui pelo menos um elemento
# e o primeiro elemento é igual ao último
# same_first_last([1, 2, 3]) -> False
# same_first_last([1, 2, 3, 1]) -> True
# same_first_last([1, 2, 1]) -> True

def same_first_last(nums):
    if len(nums) > 0 and nums[0] == nums[-1]:
        return True
    else:
        return False

# C. common_end #
# Dada duas listas a e b verifica se os dois primeiros são
# iguais ou os dois últimos são iguais
# suponha que as listas tenham pelo menos um elemento
# common_end([1, 2, 3], [7, 3]) -> True
# common_end([1, 2, 3], [7, 3, 2]) -> False
# common_end([1, 2, 3], [1, 3]) -> True

def common_end(a, b):
    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    else:
        return False

# D. maior_ponta #
# Dada uma lista não vazia, cria uma nova lista onde todos
# os elementos são o maior das duas pontas
# obs.: não é o maior de todos, mas entre as duas pontas
# maior_ponta([1, 2, 3]) -> [3, 3, 3]
# maior_ponta([1, 3, 2]) -> [2, 2, 2]

def maior_ponta(nums):
    nova_lista = []
    for i in range(len(nums)):
        if nums[0] > nums[-1]:
            nova_lista.append(nums[0])
        else:
            nova_lista.append(nums[-1])
    return nova_lista

# E. sum2 #
# Dada uma lista de inteiros de qualquer tamanho
# retorna a soma dos dois primeiros elementos
# se a lista tiver menos de dois elementos, soma o que for possível

def sum2(nums):
    if len(nums) < 2:
        return nums[0]
    else:
        return nums[0]  + nums[1]

