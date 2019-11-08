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
def StrictInequality(a,b):
    ModeA = float_input(a)
    ModeB = float_input(b)
    while ModeA==ModeB:
        ModeA = float_input()
        ModeB = float_input()
    else:
        return ModeA,ModeB
print("""
------------------
Sasha Korets KM-92
------------------
variant #4
------------------
1-open first work
2-open second work
3-open third work
other number- end 
------------------
""")
while True:
    k = int_input(input('what job to open?:'))
    if k == 1 :
        print("""
------------------------------------
Користувач уводить три числа. 
Збільшити перше число в два рази,
друге числа зменшити на 3, 
третє число звести в квадрат і
потім знайти суму нових трьох чисел.
------------------------------------
""")
        x = float_input(input('Number one:'))
        y = float_input(input('Number two:'))
        z = float_input(input('Number three:'))
        x = x * 2
        y = y - 3
        z = pow(z, 2)
        print('Number one*2: ',x)
        print('Number two-3: ',y)
        print('Number three^2: ',z)
        print('Number one*2+Number two-3+Number three^2: ',x+y+z)
    elif k == 2:
        print("""
--------------------------------
Увести з клавіатури дійсні
числа х і у, не рівні одне
одному. Менше з цих двох чисел
замінити половиною їх суми,
а більше - їх подвоєним добутком.
---------------------------------""")
        x,y = StrictInequality(input('same number:'),input('same number:'))
        print('x = ',x,'\ny = ',y)
        if x > y:
            y1 = (x + y) / 2
            print('y менше чим x, y=(x+y)/2=',y1)
            x1 = x * y * 2
            print('x більше чим y, x=y*x*2=',x1)
        else:
            x2 = (x + y) / 2
            print('x менше чим y, x=(x+y)/2=',x2)
            y2 = x * y * 2
            print('y більше чим x, y=y*x*2=',y2)
    elif k == 3:
        print("""
----------------------------
Прогарма виконує функцію
вказану нижче
----------------------------
F(x)={0,       якщо x<=1
     {1/(x+6), якщо x>1 
----------------------------
Ведіть дійсне число
----------------------------""")
        var1 = float_input(input('number:'))
        if var1 > 1:
            print(1 / (var1 + 6))
        else:
            print(0)
    else : exit('goodbye')