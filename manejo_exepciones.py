def division(num):
    division=[]
    for x in range(1,num, 1):
        if num % x ==0:
            division.append(x)
    return division

def rum ():
    try:
        num= int(input("ingrese un numero"))
        print(division(num))
        print("el programa ya termino")
    except ValueError:
        print("debes de ingresar un numero")


if __name__=='__main__':
    rum()
#