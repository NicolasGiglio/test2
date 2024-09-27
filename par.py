def es_par(num):
    return num%2==0

def solicitar_numero():
    num= int(input("ingrese numero para evaluar paridad: "))
    while num<=0:
        print("ingreso invalido")
        num= int(input("ingrese numero para evaluar paridad: "))

def main():

    num= solicitar_numero()

    if es_par(num):
        print("es par")
    else:
        print("es impar")