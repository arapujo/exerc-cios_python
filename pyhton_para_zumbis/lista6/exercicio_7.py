# G. dista10
# seja um inteiro n
# retorna True se a diferença absoluta entre n e 100 ou n e 200
# for menor ou igual a 10
# dista10(93) -> True
# dista10(90) -> True
# dista10(89) -> False
def dista10(n):
    if abs(100 - n) <= 10 or abs(200 - n) <= 10:
        
        return True
    else:
        return False

print(dista10(93))
print(dista10(90))
print(dista10(89))

