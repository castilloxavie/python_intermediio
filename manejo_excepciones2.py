def division(num):
    division = []
    for i in range(1, num + 1):
        if num % i == 0:
            division.append(i)
    return division


def run():
    while True:
        try:
            num = int(input('Ingresa un número: '))
            if num < 0:
                raise ValueError
            print(division(num))
            print("Terminó mi programa")
            break
        except ValueError:
            print("Debes ingresar un entero positivo")


if __name__ == '__main__':
    run()
#