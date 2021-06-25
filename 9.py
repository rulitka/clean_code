1. Пример проверки деления на ноль:
x = "1/0"
try:
    print(1/0)
except ZeroDivisionError:
    print ("WARNING: Invalid Equation")
    
2. Примеры преобразования типов в Python:
int(‘123’) вернет целое число 123
str(123) вернет строку ‘123’
list('abc') = ['a', 'b', 'c'] преобразует строку в список букв

3. Пример целочисленного деления:
print(5 // 2)
print(0 // 2)
print(1234 // 5.0)

4. Пример использования модуля Decimal для предотвращения переполнеия целых чисел:
import sys
from decimal import Decimal

print('max size = ', sys.maxsize)
number = Decimal("8e10000000")
print(number)

5. 
