def division(num):
    division=[]
    for x in range(1,num +1):
        if num % x ==0:
            division.append(x)
    return division



def rum ():
    num = int(input("ingresa un numero"))
    print(division(num))
    print("termino mi prograna")






if __name__ =='__main__':
    rum()
#