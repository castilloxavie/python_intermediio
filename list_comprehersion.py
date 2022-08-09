def rum():
    #squares=[]     # ejemplos de raiz cuadrada
    #for i in range(1,101):
        #if i % 3 !=0:
            #scuares.append(i**2)

    scuares=[x**2 for x in range(1,101) if x % 3!=0]
    print(scuares)

    print("---------------------------------------------------------")

    raiz_cua=[ x ** 4 for  x in range(2, 1000, 2) if x % 4 ==0 and x % 8==0]
    print(raiz_cua)


    



if __name__=='__main__':
    rum()
#