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

4. Пример  использования функции round для округления до второго знака после запятой:
round(x, 2)

5. Пример использования модуля Decimal для предотвращения переполнеия целых чисел:
import sys
from decimal import Decimal

print('max size = ', sys.maxsize)
number = Decimal("8e10000000")
print(number)

6.Пример использования типа данных Decimal с большей точностью, чем float:
from decimal import Decimal    
Decimal(2.675)
Decimal('2.67499999999999982236431605997495353221893310546875')

7. Пример использования типа данных Fraction с большей точностью, чем float:
from fractions import Fraction
Fraction(1, 3**54)
Fraction(1, 58149737003040059690390169)

8. Пример использования булева типа данных:
def check_human_in_video(video):
    human_found = False
    for frame in video:
        if frame.has_human():
            human_found = True
    print(human_found)
