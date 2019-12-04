import re
from int_and_float_validation import *
from start_info_about_me import start_info


def check(myStr):
    # Python3 code to Check for
    # balanced parentheses in an expression
    # Function to check parentheses
    open_list = ["[", "{", "("]
    close_list = ["]", "}", ")"]
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if ((len(stack) > 0) and
                (open_list[pos] == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Unbalanced"
    if len(stack) == 0:
        return "Balanced"


def FunctionProcessing(text):
    '''
        #функ перевіряє введене рівняння користувача, якщо воно має якісь інші символи окрім заданих, то функ просить ввести рівняння заново
    :param text:
    :return:
    '''
    valid = re.findall('[x,i,\*,\-,\+,\.,\d,\),\(,\/,\%,\ ]', text)
    same_time_var = text
    while True:
        if len(valid) == len(same_time_var) and check(same_time_var) == "Balanced" :
            break
        else:
            same_time_var = input('write your func again: ')
            valid = re.findall('[x,i,\*,\-,\+,\.,\d,\),\(,\/,\%,\ ]',same_time_var)
    return same_time_var





def SumaOfSameRivniannia(data_equation):
    n = int_input(input('Введіть n:'))
    if len(re.findall('x',data_equation)) != 0:
        x = float_input(input('Введіть x:'))
    sum_end = float(0)
    for i in range(1, n + 1):
        sum = eval(data_equation)
        sum_end = sum + sum_end
        i += 1
    resust = 'suma first {0} chleniv= {1}'.format(n, sum_end)
    return resust

def FuncForSecondTask(stop_simvol):
    '''
        function creates a loop that allows you to continuously enter integers until you enter a special(:param stop_simvol) character
    :param stop_simvol: (int)
    :return: sum (int) all chleniv without last(:param stop_simvol),kilkist (int) all chleniv without last(:param stop_simvol),ser_arefmetic or sum/kilkist (float)
    '''
    sum = 0
    kilkist = 0
    i = None
    while i != stop_simvol:
        i = int_input(input('ведіть будь-яке ціле чсило :'))
        kilkist += 1
        sum = i + sum
    return  sum-stop_simvol,kilkist-1,(sum-stop_simvol)/(kilkist-1)

start_info()

print("""
***1  -  first work***
***2  - second work***
***other-close work***
""")
while True:
    k = input('what job to open?:')
    if k == '1':
        print('***************\nn\n---\n\  your func(for example: (x+i)/i)\n/\n---\ni=1\n***************')
        var1 = FunctionProcessing(input('your func: '))
        print('***************\nn\n---\n\  {0}\n/\n---\ni=1\n***************'.format(var1))
        print(SumaOfSameRivniannia(var1))
    elif k=='2' :
        print('''-------------------------------------\nОрганізувати безперервне введення\nцілих чисел з клавіатури, поки\nкористувач не введе задане число t. Після\nвведення t, показати на екрані кількість\nчисел, які були введені, їх загальну\nсуму і середнє арифметичне.\n-------------------------------------''')
        t = int_input(input('ведіть закриваюче ціле число "t": '))
        print('''\n-------------------------------------\nОрганізувати безперервне введення\nцілих чисел з клавіатури, поки\nкористувач не введе задане число t. Після\nвведення {0}, показати на екрані кількість\nчисел, які були введені, їх загальну\nсуму і середнє арифметичне.\n-------------------------------------'''.format(t))
        result_sum,kilkist,ser_arefmetic = (FuncForSecondTask(t))
        print('*******************\nsum all numbers without last: {}\nkilkist all numbers without last: {}\nthe atithmetic mean: {}\n*******************'.format(result_sum,kilkist,ser_arefmetic))
    else:
        exit('good bye')


