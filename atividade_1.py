primos = [2,3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
quantidade = 0
for numero in primos:
    if numero < 67:
        quantidade += 1

print("Quantidade de números primos menores que 67:", quantidade)