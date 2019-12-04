from int_and_float_validation import *
from start_info_about_me import start_info

def StrictInequality(a,b):
    '''
        func returne a and b if a!=b, else агтс asks to enter again
    :param a:(float)
    :param b:(float)
    :return: (:param a),(:param b)
    '''
    A = float_input(a)
    B = float_input(b)
    while A==B:
        A = float_input(input('same number again 1 :'))
        B = float_input(input('same number again 2 :'))
    else:
        return A,B

start_info()


#**********************************************************
# я неписав функ для кожної під програми, вони занадто малі
#також не написав функ для повторення програми, незміг
#**********************************************************

print("""
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
        x,y = StrictInequality(input('same number 1 :'),input('same number 2 :'))
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