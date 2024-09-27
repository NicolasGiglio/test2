def main():
    num= int(input("ingrese numero para evaluar paridad: "))
    es_par= num%2==0
    if es_par:
        print("es par")
    else:
        print("es impar")