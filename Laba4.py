def pora_roku(x):
    while x!=1 and x!=2 and x!=3 and x!=4:
        var1 = 0
        if x == '1':
            var1='зима має 90(91) днів, грудень 31, січень 31, лютий 28(29)'
        elif x == '2':
            var1='весна має 92 дні, березень 31, квітень 30, травень 31'
        elif x == '3':
            var1='літо має 92 дні, червень 30, липень 31, серепень 31'
        elif x == '4':
            var1='осінь має 91 день, вересень 30, жовтень 31, листопад 30'
    else:
        var1 = ''
    return var1

def new_funk(data_text,t='t'):
    data_list=list(data_text)
    for index, simvol in enumerate(data_list[0:len(data_list):1]):
        #print(index, simvol)
        if simvol ==t:
            new_list = data_list[:index] + [' "тут відбувся розрив, {0} викидається" '.format(t)] + data_list[index+1:]
            new_text = ''.join(new_list)
            print(new_text)
            break
        else:
            continue
        return new_text


print('''
-----------------
Korets  Oleksandr
KM-92 		var-4
-----------------
''')
while True:
    print('''
    ------------------------
    1-open firts 
    2-open second
    other-exit
    ------------------------
    ''')
    number_of_job=input('what do you open wokr?')
    if number_of_job=='1':
        while True:
            print('''
            ---------
            1-winter
            2-sprint
            3-sammer
            4-autem
            other-back
            ---------
            ''')
            part_of_year=input('same number:')
            print(pora_roku(part_of_year))
            if part_of_year!='1' and part_of_year!='2' and part_of_year!='3' and part_of_year!='4':
                break
    elif number_of_job=='2':
        data=input('input same text:')
        simvol_rozbutia=input('sumvol_of_rozbutia:')
        print(new_funk(data,simvol_rozbutia))
    else:
        exit('goodbye')