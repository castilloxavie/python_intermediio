def division(num):
    division = []
    for i in range(1, num + 1):
        if num % i == 0:
            division.append(i)
    return division


def run():
    num = input('Ingresa un número: ')
    assert num.isnumeric(), "Debes ingresar un número"
    print(division(int(num)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()
#