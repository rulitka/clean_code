7.1 правильное именование булевых переменных в вашем коде в формате "было - стало".
- Flag = True – conditionComplete  = True 
//задача 27
- Flag = True – NumberOfLetterIsOk = True 
//задача 22
- Flag = True  - AllLettersIsDiffer = True 
//задача 21
- Flag = False  - HistoryWasReset  = False
//так как в начале программы история еще не обнулялась, эта переменная равно False, и в тот момент, когда происходит операция обнуления истории, эта переменная становится True (задача 20)
- Flag = False  - arrayGrow= False  
//задача 18

7.2 типичные имена булевых переменных в вашем коде
- задача 27 – можно использовать имя success, так как флаг равен True, когда условие соблюдается.
- задача 21 –можно использовать имя found, так как флаг равен True, когда найдено магическое слово.
- задача 18 – можно использовать имя error, так как начальным условием флага является то, что массив не упорядочен по возрастанию.

7.3 имена индексов циклов
   for x in new:
        if subs in x:
            for i, t in enumerate(x):
// задача №7, в этой задаче несколько вложенных циклов, и для перебора этих циклов трех стандартных букв i, j, k недостаточно.
for _ in range(0, 2): -                 for element in range(0, 2):
// В задаче №18, вместо символа _ можно использовать слово «элемент», так как символ _ вообще не несет никакой смысловой нагрузки.

7.4 пары имён – антонимов
- first_transform/second_transform - first_transform/last_transform
//задача 25
- F/F_sort - F/F_after_sorting
// задача 27
- new_matrix/ convert_array/ result – array_begin/array_convert_to_bool/array_end
// задача 28
- new_matrix/ pretty_matrix – matrix_before/matrix_after
//задача 24

7.5 выразительные имена временных переменных
-  temp_matrix - ChangeThreeDigits
- tmp – currElemArrayForTurn (curren_Element_Array_For_Turn)
