def convert_decimal_to_base(n, base):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(str(n % base))
        n //= base
    return ''.join(digits[::-1])

def convert_base_to_decimal(n, base):
    decimal = 0
    power = len(n) - 1
    for digit in n:
        decimal += int(digit) * (base ** power)
        power -= 1
    return decimal

def main():
    print("Добро пожаловать в калькулятор для перевода чисел из одной системы счисления в другую!")
    while True:
        choice = input("Выберите действие:\n1. Перевести число из десятичной в другую систему счисления\n2. Перевести число из другой системы счисления в десятичную\n3. Выйти\nВаш выбор: ")
        if choice == '1':
            num = int(input("Введите число в десятичной системе счисления: "))
            base = int(input("Введите целевую систему счисления (2-16): "))
            print(f"Результат: {convert_decimal_to_base(num, base)}")
        elif choice == '2':
            num = input("Введите число: ")
            base = int(input("Введите систему счисления исходного числа (2-16): "))
            print(f"Результат: {convert_base_to_decimal(num, base)}")
        elif choice == '3':
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()