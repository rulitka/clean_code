1. Задача №4. 
// Инициализация переменных перенесена поближе к моменту их использования:
// Было
    lst_new = []
    lst_curr = []
    // ... много кода
    for i in range(len(Tele_new)):
        if i <= center:
            lst_new.append(Tele_new[i])
        if i > center:
            lst_curr.append(Tele_new[i])
// Стало
    lst_new = []
    lst_curr = []
    for i in range(len(Tele_new)):
        if i <= center:
            lst_new.append(Tele_new[i])
        if i > center:
            lst_curr.append(Tele_new[i])
 
2. Задача №4.
// Убрана строка с  присвоением переменной значения заранее:
// Было
    string_result = 0
    // ... много кода
    string_result = ''
    old_with_null = '0'
    new_no_null = ''
    for i in string_no_point:
        if i == old_with_null:
            i = new_no_null
        string_result += i
// Стало
    string_result = ''
    old_with_null = '0'
    new_no_null = ''
    for i in string_no_point:
        if i == old_with_null:
            i = new_no_null
        string_result += i
        
3. Задача №15.
// Инициализация переменных перенесена поближе к моменту их использования:
// Было
    pre_result_S1 = create_matrix(H1, W1, S1)
    pre_result_S2 = create_matrix(H2, W2, S2)
    // ... много кода
    for i in range(len(pre_result_S1)): 
        for j in range(len(pre_result_S1[i])):
            if pre_result_S2 == tmp:
    // ... дальше код
// Стало
    pre_result_S1 = create_matrix(H1, W1, S1)
    pre_result_S2 = create_matrix(H2, W2, S2)
    for i in range(len(pre_result_S1)): 
        for j in range(len(pre_result_S1[i])):
            if pre_result_S2 == tmp:
    // ... дальше код
    
4.Задача №15.
// Убрана строка с  присвоением переменной значения заранее:
// Было  
    pre_result_S1 = create_matrix(H1, W1, S1)
    pre_result_S2 = create_matrix(H2, W2, S2)
    tmp = [[0] * W2 for i in range(H2)]
    x = 0
    y = 0
    num = 0
    lum = 0
    for i in range(len(pre_result_S1)): 
        for j in range(len(pre_result_S1[i])):
     // ... дальше код         
// Стало
    pre_result_S1 = create_matrix(H1, W1, S1)
    pre_result_S2 = create_matrix(H2, W2, S2)
    tmp = [[0] * W2 for i in range(H2)]
    x = 0
    y = 0
    for i in range(len(pre_result_S1)): 
        for j in range(len(pre_result_S1[i])):
     // ... дальше код
    
5. Задача №15.
// Убрана строка с  присвоением переменной значения заранее:
// Было
    result_S = []
    result_S = [0] * H
// Стало
    result_S = [0] * H
  
6.Задача №15.
// Инициализация переменных перенесена поближе к моменту их использования:
// Было
def create_matrix(H, W, S):
    result_S = []
    result_S = [0] * H
    a = 0
    j = 0
    
    for i in range(H):
        result_S[i] = [0] * W
    
    for i in range(len(S)):
        if S[i] == ' ':
            a += 1
            j = 0
            pass
        else:
            result_S[a][j] = int(S[i])
            j += 1
            continue
    return result_S
// Стало
def create_matrix(H, W, S):
    result_S = [0] * H    
    for i in range(H):
        result_S[i] = [0] * W

    a = 0
    j = 0
    for i in range(len(S)):
        if S[i] == ' ':
            a += 1
            j = 0
            pass
        else:
            result_S[a][j] = int(S[i])
            j += 1
            continue
    return result_S
7. Задача №20:
// Инициализация переменной перенесена поближе к моменту ее использования:
//Было
  def BastShoe(command):
    check_str = check_string(command)
    final_elem = ''
    global final_string
    if check_str[0] == 1:
        final_string = add_string(check_str)
    if check_str[0] == 2:
        final_string = del_elements(check_str)
    if check_str[0] == 3:
        final_elem = get_index_element(check_str)
        return final_elem
    if check_str[0] == 4:
        final_string = undo_position()
    if check_str[0] == 5:
        final_string = redo_position(check_str)
    return final_string
//Стало
  def BastShoe(command):
    check_str = check_string(command)
    global final_string
    if check_str[0] == 1:
        final_string = add_string(check_str)
    if check_str[0] == 2:
        final_string = del_elements(check_str)
    final_elem = ''
    if check_str[0] == 3:
        final_elem = get_index_element(check_str)
        return final_elem
    if check_str[0] == 4:
        final_string = undo_position()
    if check_str[0] == 5:
        final_string = redo_position(check_str)
    return final_string
  
8. Задача №21
// Убарана лишняя переменная, которая дальше в программен не была задействована:
// Было
def oddswap(in_put):
    temp_matrix = list(in_put)
    full_matrix = []
    part_matrix= []
// Стало
def oddswap(in_put):
    temp_matrix = list(in_put)
    full_matrix = []

9. Задача №26
// Инициализация переменной перенесена поближе к моменту ее использования:
// Было
def BalancedParentheses(N):
    global combs
    combs = []
    combinations(N, left = N, right = N, toClose = 0, str="")
    result = ' '.join(combs)
    return result
// Стало
def BalancedParentheses(N):
    global combs
    combinations(N, left = N, right = N, toClose = 0, str="")
    combs = []
    result = ' '.join(combs)
    return result
  
10. Задача №27
//Исправлена ошибка переменная length была инициализирована, но не была использована:
//Было
def rule_one(F):
    Flag = True
    n = 0
    m = 0
    length = len(F)
    pos1 = 0
    pos2 = 0
    for i in range(1, len(F)):
    // Дальше код
// Стало
def rule_one(F):
    Flag = True
    n = 0
    m = 0
    length = len(F)
    pos1 = 0
    pos2 = 0
    for i in range(1, length):
    // Дальше код
 
11. Задача №2
// Размещение переменной-счетчика непосредственно перед циклом:
//Было
        num = 0
        sum_distance = 0
        distance_all = 0
        for index, number in enumerate(N):
            if index%2 == 0:
                speed = N[index]
            else:
                if num == 0:
                    time = N[index]
                    num=+1
                    distance = speed*time  
                else:
                    time_new = N[index] - time
                    time = N[index]
                    distance = speed*time_new
                sum_distance += distance
        distance_all += sum_distance
        return distance_all
    else:
        exit() 
//Стало
        sum_distance = 0
        distance_all = 0
        num = 0
        for index, number in enumerate(N):
            if index%2 == 0:
                speed = N[index]
            else:
                if num == 0:
                    time = N[index]
                    num=+1
                    distance = speed*time  
                else:
                    time_new = N[index] - time
                    time = N[index]
                    distance = speed*time_new
                sum_distance += distance
        distance_all += sum_distance
        return distance_all
    else:
        exit()
12. Задача № 3
// Размещение переменной-счетчика непосредственно перед циклом:
// Было 
def ConquestCampaign(N, M, L, battalion):
    board = [[0]*M for i in range(N)]
    day = 1
    count = N*M
    
    for i in range(0, 2*L, 2): 
        x = battalion[i] - 1 
        y = battalion[i+1] - 1 
        if board[x][y] == 0:
            board[x][y] = 1
            count -= 1
            
    while count != 0:
        new_board = [[board[i][j] for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                if board[i][j] == 1:
                    for x, y in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                        if 0 <= x < N and 0 <= y < M and new_board[x][y] == 0:
                            new_board[x][y] = 1
                            count -= 1
        board = new_board
        day += 1
    return day
// Стало
def ConquestCampaign(N, M, L, battalion):
    board = [[0]*M for i in range(N)]
    count = N*M
    
    for i in range(0, 2*L, 2): 
        x = battalion[i] - 1 
        y = battalion[i+1] - 1 
        if board[x][y] == 0:
            board[x][y] = 1
            count -= 1
    
    day = 1            
    while count != 0:
        new_board = [[board[i][j] for j in range(M)] for i in range(N)]
        for i in range(N):
            for j in range(M):
                if board[i][j] == 1:
                    for x, y in (i-1, j), (i, j-1), (i, j+1), (i+1, j):
                        if 0 <= x < N and 0 <= y < M and new_board[x][y] == 0:
                            new_board[x][y] = 1
                            count -= 1
        board = new_board
        day += 1
    return day

13. Задача №12
// Размещение переменной-счетчика непосредственно перед циклом:
// Было
def MassVote(N, Votes):
    mx = Votes[0]
    n = 0
    for i in range(len(Votes)):
        if Votes[i] > mx:
            mx = Votes[i]
    for i in range(len(Votes)):
        if mx == Votes[i]:
            n += 1
    // Дальше код

// Стало
def MassVote(N, Votes):
    mx = Votes[0]
    for i in range(len(Votes)):
        if Votes[i] > mx:
            mx = Votes[i]
    n = 0
    for i in range(len(Votes)):
        if mx == Votes[i]:
            n += 1
    // Дальше код

14. Задача №14
// Размещение переменной-счетчика непосредственно перед циклом:
// Было
def Unmanned(L, N, track):
    num = 0
    number_of_tr_light = 0
    real_time = 0
    for i in range(1, L+1):
        tr_light = track[number_of_tr_light][0]
        if i == tr_light:
            real_time += 1
            num += 1
// Стало
def Unmanned(L, N, track):
    number_of_tr_light = 0
    real_time = 0
    num = 0
    for i in range(1, L+1):
        tr_light = track[number_of_tr_light][0]
        if i == tr_light:
            real_time += 1
            num += 1
15. Задача № 16
// Размещение переменной-счетчика непосредственно перед циклом:
// Было
def create_matrix(N, price):
    H = 3 
    W = (int(N / H) + (N % H > 0)) 
    result_S = []
    result_S = [0] * W
    a = 0
    j = 0
    n_elem = 0
    for i in range(W):
        result_S[i] = [0] * H
    
    for i in range(len(price)):
        if n_elem < 3:
            result_S[a][j] = int(price[i])
            j += 1
            n_elem += 1
        if n_elem == 3:
                a += 1
                j = 0
                n_elem = 0
    return result_S
// Стало
def create_matrix(N, price):
    H = 3 
    W = (int(N / H) + (N % H > 0)) 
    result_S = []
    result_S = [0] * W
    a = 0
    j = 0
    for i in range(W):
        result_S[i] = [0] * H
    
    n_elem = 0    
    for i in range(len(price)):
        if n_elem < 3:
            result_S[a][j] = int(price[i])
            j += 1
            n_elem += 1
        if n_elem == 3:
                a += 1
                j = 0
                n_elem = 0
    return result_S
