1. Связывание происходит в момент написания кода.
// Задача №22
// number это счетчик, поэтому этой переменной в самом начале присваивается значени ноль.
def SherlockValidString(s):
    number = 0
    
2. Связывание происходит во время компиляции кода.
//Задача №23
// На вход функция получает переменную new_matrix, значение которой присваивается переменной pre_result для дальнейших вычислений.
def convert_to_symbol(new_matrix):
    pre_result = new_matrix
   
3. Связывание происходит во время выполнения программы.
//Задача №22
//Здесь переменной count_dict значение присваивается во время выполнения программы, когда вызывается функция create_dict(s)
def SherlockValidString(s):
    ...
    count_dict = create_dict(s)
