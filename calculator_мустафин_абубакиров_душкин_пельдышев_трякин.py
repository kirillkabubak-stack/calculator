def add(a, b):

    return a + b

def subtract(a, b):

    return a - b

def multiply(a, b):

    return a * b

def divide(a, b):

    if b == 0:
        return "Ошибка: Деление на ноль!"
    return a / b

def power(a, b):

    return a ** b

def main():

    print("Калькулятор")
    print("Доступные операции:")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (**)")
    
    try:
        
        num1 = float(input("Введите первое число: \n"))
        
        operation = input("Введите операцию (+, -, *, /, **): \n")
        
        num2 = float(input("Введите второе число: \n"))
        
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        elif operation == '**':
            result = power(num1, num2)
        else:
            result = "Ошибка. Неизвестная операция!"
        
        print(f"Результат: {num1} {operation} {num2} = {result}")
        
    except ValueError:
        print("Ошибкa. Введите корректные числа!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()