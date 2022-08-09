from numpy import floating, integer


def rum():
    my_list=[1, "hola", True, 2.3]
    my_dict={"firstname":"xavier", "lastname":"castillo"}

    super_lis=[
        {"firsname":"angi", "lastname":"ramirez"},
        {"firsname":"paola", "lastname":"varon"},
        {"firsname":"emelina", "lastname":"ochoa"},
        {"firsname":"norma", "lastname":"fredery"},

    ]

    super_dict={
        "natural_num1":[1,2,3,4,5,6,7,8,9],
        "integer_num1":[-1, -2, 3, 4],
        "floating_num1":[1.2, 3.4, 56]

    }
    for key, values in super_dict.items():
        print(key, "-", values)

    print(super_lis[::])

if __name__== '__main__':
    rum() 
#