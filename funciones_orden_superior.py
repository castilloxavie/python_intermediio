from functools import reduce
#uso del filter

my_list= [1,4,5,6,9,13,19,21,22]

xfilter=list(filter(lambda x: x%2 !=0, my_list))
print(xfilter)
print('----------------------------xfilter--------------------------')


# uso de map

myLista=[1,2,3,4,5]
squares= [x**2 for x in myLista]
print(squares)

myLista=[1,2,3,4,5]
xmap =list(map(lambda m: m**2 ,myLista))
print(xmap)
print('----------------------------xmap--------------------------')

#uso de reduce
milista=[2,2,2,2,2]
xreduce= reduce[lambda a, b: a*b, milista]
print(xreduce)
#