def es_par(num):
    return num%2==0

def main():

    num= int(input("ingrese numero para evaluar paridad: "))
    
    if es_par(num):
        print("es par")
    else:
        print("es impar")