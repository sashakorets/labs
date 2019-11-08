import re
def int_input(text):
    pattern_int = r"^[-\d]\d*$"
    user_input = text
    while not re.match(pattern_int, user_input):
        user_input = input("Enter int:")
    return int(user_input)
def float_input(text):
    pattern_float = r"^\d+\.?\d*$"
    user_input = text
    while not re.match(pattern_float, user_input):
        user_input = input("Enter float:")
    return float(user_input)
def SumaOfSameRivniannia(data_funk):
    n = int_input(input('Введіть n:'))
    x = float_input(input('Введіть x:'))
    sum_end = float(0)
    for i in range(1, n + 1):
        sum = eval(data_funk)
        sum_end = sum + sum_end
        i += 1
    resust = 'suma first {0} chleniv= {1}'.format(n, sum_end)
    return resust
def FunctionProcessing(text):
    valid = re.findall('[x,i,\*,\-,\+,\.,\d.\),\(,\/,\%,\ ]', text)
    while len(valid) == len(text):
        return text
        break
    else:
        text = input('write your func again: ')
def FuncForSecondTask(siparator):
    n = 0
    sum = 0
    kilkist = 0
    i = None
    while i != siparator:
        i = int_input(input('ведіть будь-яке ціле чсило :'))
        kilkist += 1
        sum = i + sum
    return  sum-siparator,kilkist-1,(sum-siparator)/(kilkist-1)
print("""   
***Korets Oleksandr***
***KM-92  Variant-4***
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
        print('''
-------------------------------------
Організувати безперервне введення
цілих чисел з клавіатури, поки 
користувач не введе задане число t. Після
введення t, показати на екрані кількість
чисел, які були введені, їх загальну 
суму і середнє арифметичне.
-------------------------------------''')
        t = int_input(input('ведіть закриваюче ціле число "t": '))
        print('''
-------------------------------------
Організувати безперервне введення
цілих чисел з клавіатури, поки 
користувач не введе задане число t. Після
введення {0}, показати на екрані кількість
чисел, які були введені, їх загальну 
суму і середнє арифметичне.
-------------------------------------'''.format(t))
        result_sum,kilkist,ser_arefmetic = (FuncForSecondTask(t))
        print('*******************\nsum all numbers without last: {}\nkilkist all numbers without last: {}\nthe atithmetic mean: {}\n*******************'.format(result_sum,kilkist,ser_arefmetic))
    else:
        exit('good bye')
