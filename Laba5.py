from start_info_about_me import start_info

def NumberOfWordsInFirtsTextEqualNumberOfWordsInSecondText(FirstString,SecondString):
    '''
    siparator = ' '
    :param FirstString:(str) - same text
    :param SecondString:(str) - same text
    :return: list(FirstString) , list(SecondString)
    '''
    while True:
        FirstList = FirstString.split(' ')
        SecondList = SecondString.split(' ')
        #print(len(FirstList))
        #print(len(SecondList))
        if len(FirstList) == len(SecondList):
            break
        else:
            FirstString = input('enter text1 again')
            SecondString = input('enter text2 again')
    return FirstList, SecondList
def RemoveLongerWords(list1,list2):
    '''
        funk compares len(element[i]) of list1 and len(element[i]) of list2
        if same element[i] of list1 bigger len(element[i]) of list2, funk remove him
        if element[i] of list1==element[i] of list2 , funk remove two element
    :param list1:(list)
    :param list2:(list)
        len(list1)==len(list1)
    :return: mode list1,list2
    '''
    n1 = 0
    n2 = 0
    for i in range(len(list1)-n1) :
        if len(list1[i-n1]) > len(list2[i-n2]) :
            del list1[i-n1]
            n1 += 1
        elif len(list1[i-n1]) < len(list2[i-n2]) :
            del list2[i-n2]
            n2 += 1
        elif len(list1[i-n1]) == len(list2[i-n2]) :
            del list1[i-n1]
            del list2[i-n2]
            n1 += 1
            n2 += 1

    if len(list1)==0 and len(list2)==0:
        list2.append('is clean')
        list1.append('is clean')
    elif len(list1)==0:
        list1.append('is clean')
    elif len(list2)==0:
        list2.append('is clean')
    return list1,list2

start_info()


while True:
    print('''
-----------------
1-open firts 
2-open second
other-exit
-----------------
    ''')
    number_of_job=input('what do you open wokr?')
    if number_of_job=='1':
        print('''
        Створити 2 списки, однакової довжини за кількістю слів. Необхідно:
            - порівняти слова на однакових позиціяї і видалити більше;
            - якшо слова однакові по довжиніЮ видалити обидва;
            - вивести на екран обидва модифікованих списки.
        ''')
        FirstList, SecondList = NumberOfWordsInFirtsTextEqualNumberOfWordsInSecondText(input('enter text1'),
                                                                                       input('enter text2'))
        print(FirstList)
        print(SecondList)
        SameTimeVar1,SameTimeVar2 = RemoveLongerWords(FirstList,SecondList)
        print('out put :\nlist 1 : {0}\nlist 2 : {1}'.format(SameTimeVar1,SameTimeVar2))
    elif number_of_job == '2':
        print('A = {*element}, B = {*element}, F = ((A⊕B)∩(A∪B))')
        A = set(input('input same set1'))
        B = set(input('input same set2'))
        print('set1 :{0}\nset2 :{1}'.format(A,B))
        C = A.symmetric_difference(B)
        print('set3 = symmetric difference set1 and set2 :',C)
        D = A.union(B)
        print('set4 = union set1 and set2 :',D)
        E = C.intersection(D)
        print('the intersection of set3 and set4 :',E)
    else:
        exit('goodbye')

