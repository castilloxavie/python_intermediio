def rum():
     
     dic={i: i ** 3 for i in range(1, 100) if i % 3 != 0}
     print(dic)

     print("-----------------------")

     other={x: x ** 2 for x  in range (1, 1001)  if x % 2==0 and x % 3 ==0 and x % 8==0 }
     print(other)

     print("-------------------------------------------------")

     print(dic, other)

    


if __name__=='__main__':
    rum()
#