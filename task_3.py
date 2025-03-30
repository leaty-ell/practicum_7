import math
def square(num):
    root = math.isqrt(num)
    return root * root == num

while True:
    try:
        number = int(input("Введите число: "))
        if square(number):
            print(f"Число {number} является полным квадратом!")
            break
        else:
            print(f"Число {number} не является полным квадратом. Попробуйте ещё раз.")
    except ValueError:
        print("Ошибка: Введите целое число.")
