def es_primo(num: int, i=2) -> bool:
    if num < 2:
        return False
    if i >= num:
        return True
    if num % i == 0:
        return False
    
    return es_primo(num, i + 1)

num = int(input("Ingrese un número: "))
if es_primo(num):
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")