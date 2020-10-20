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

print(same_first_last([1, 2, 3]))
print(same_first_last([1, 2, 3, 1]))

