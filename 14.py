// Комментарии нужны:
  
1.	Задача 27
def rule_one(F):#поменять местами два произвольных элемента
def rule_two(F_temp):#изменить на обратный порядок
// Здесь комментарий уместен, потому что в задании мы должны использовать  два правила, и логично описать, каждое из них.

2.	Задача 27
def check_one(F):
    Flag = True #значально считает, что список возрастает
    n = 0 #показатель возрастания
    m = 0 #показатель убывывания
// Здесь комментарий нужен, чтобы мы понимали, что изначально подразумевается в переменной Flag.

3.	Задача 10
# Если встречается символ, не учитываемый таблицей из документации, используйте значение 23
//Это важный комментарий,  поясняющий условие задачи

4.	Задача 16
def create_matrix(N, price):
    H = 3 #количество столбцов(равно количеству элементов в строке)
    W = (int(N / H) + (N % H > 0))  #количество строк (округление в большую сторону)
//Здесь комментарий уместен, как как в имени переменной сложно было бы уместить всю эту информацию.

5.	Задача 24
# Function to rotate a matrix
def rotateMatrix(mat):

    if not len(mat):
        return

    """
        top : starting row index
        bottom : ending row index
        left : starting column index
        right : ending column index
    """

    top = 0
    bottom = len(mat)-1

    left = 0
    right = len(mat[0])-1

    while left < right and top < bottom:

        # Store the first element of next row,
        # this element will replace first element of
        # current row
        prev = mat[top+1][left]

        # Move elements of top row one step right
        for i in range(left, right+1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr

        top += 1

        # Move elements of rightmost column one step downwards
        for i in range(top, bottom+1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr

        right -= 1

        # Move elements of bottom row one step left
        for i in range(right, left-1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr

        bottom -= 1

        # Move elements of leftmost column one step upwards
        for i in range(bottom, top-1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr

        left += 1

    return mat
// Эти комментарии больше похожи даже не на комментарии, а на инструкцию.

6.	Задача 27
def check_one(F):#проверяем массив убывает или возрастает
    Flag = True # массив возрастает первый элемент меньше всех остальных
    for i in range(1, len(F) - 1):
        if F[i] > F[0]:
            continue
        if F[i] < F[0]:
            Flag = False # массив убывает первый элемент больше всех остальных
    return Flag
// Здесь комментарий нужен, чтобы мы понимали, что изначально подразумевается в переменной Flag.

7.	Задача 26
# Python3 program to
# Print all combinations
# of balanced parentheses

# Wrapper over _printParenthesis()
def printParenthesis(str, n):
	if(n > 0):
		_printParenthesis(str, 0, n, 0, 0);
						
	return;
// Здесь комментарий уместен, перед кодом программы идет короткое описание того, для какой версии Python написана программа, а также, что она делает.

// Комментарии не нужны:
1.	Задача 27

def check_one(F):
    …
    n = 0 #показатель возрастания
    m = 0 #показатель убывывания
              // Здесь комментарии не нужны, нужно просто заменить имена переменных на более осмысленные, например, up = 0, down = 0 или  raise = 0 , fall = 0

2.	def rule_two(F):
    F_new = F[::-1] #разворот списка
    return F_new
               // Здесь комментарий не нужен, так как это стандартная операция

3.	        if n < 2:
            Flag = False #Один символ стоит не на своем месте, мы ничего с этим не сможем сделать    	
        if n == 2:
        	temp_result = rule_one(F) #меняем два символа местами, которые стоят не на своем месте
        if n > 2:
            half_result = check_monotone(F)# проверяем, рядом ли стоят символы, которые не на своем месте, и если рядом, делаем сорт, если не рядом, возвращаем фолз
//Комментарии слишком многословны. Имена функций должны быть просто более говорящие

4.	    n = 0 #количество раз, сколько мы вызвали приемов
// Здесь комментарий не нужен, нужно просто заменить имя переменной на более осмысленное, например, number_of_reception

5.	def check_similar(in_put): #проверяем на одинаковые буквы
// Здесь комментарий не нужен, так как название функции говорит само за себя.

