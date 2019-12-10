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
    for i in range(0,len(list1)-1) :
        if len(list1[i]) > len(list1[i]) :
            del list1[i]
        elif len(list1[i]) < len(list1[i]) :
            del list2[i]
        elif len(list1[i]) == len(list1[i]) :
            del list2[i]
            del list1[i]
    if len(list1)==0:
        list1.append('list1 is clean')
    elif len(list1)==0:
        list2.append('list2 is clean')
    return list1,list2
print('''
-----------------
Korets Oleksandr
KM-92   var-4
-----------------
''')
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
        FirstList, SecondList = NumberOfWordsInFirtsTextEqualNumberOfWordsInSecondText(input('enter text1'),
                                                                                       input('enter text2'))
        #print(FirstList)
        #print(SecondList)
        SameTimeVar1,SameTimeVar2 = RemoveLongerWords(FirstList,SecondList)
        print(SameTimeVar1,'\n',SameTimeVar2)
    elif number_of_job == '2':
        A = set(input('input same set1'))
        B = set(input('input same set2'))
        C = A.symmetric_difference(B)
        print(C)
        D = A.union(B)
        print(D)
        E = C.intersection(D)
        print(E)
    else:
        exit('goodbye')