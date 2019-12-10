import os
import random
def creat_random_list():
    '''
        just no comment
    :return:
    '''
    data_list = []
    for k in range(25):
        a = random.randint(-9,9)
        data_list.append(a)
    print(data_list)
    return data_list
def check_name_file(name_file1):
    '''
        func check file only in direktory this file 'Laba7.py'
    :param name_file1:
    :return:
    '''
    if os.path.exists(name_file1):
        print("Зазначений файл існує")
        return name_file1
    else:
        print("Файл не існує")
        k = input('create? - 1\nexit - other')
        if k == '1':
            try:
                open('{}'.format(name_file1), 'w+')
                return name_file1
            except:
                print("error, i can't create thise file")
                name_file1 = input("введіть ім'я вашого файлу : ")
            return name_file1
        else:
            exit('goodbye')


def write_smaller_then_0(name_file):
    '''
        func write all number how > 0 on file(param(name_file))
    :param name_file:
    :return:
    '''
    my_file = open('{}'.format(name_file), 'w+')
    for n in creat_random_list():
        if float(n) < 0 :
            my_file.writelines(str(n)+'\n')
        else:
            continue
    my_file.close()
def read_and_print_all_info(name_file):
    '''
        just read and print this info
    :param name_file:
    :return:
    '''
    f = open('{}'.format(name_file), 'r')
    for line in f:
        print(line[0 : len(line) - 1])
    f.close()
k = '1'
while k == '1':
    just_var = check_name_file(input("введіть ім'я вашого файлу : "))
    write_smaller_then_0(just_var)
    read_and_print_all_info(just_var)
    k = input('**********************\nreapet - 1\nexit - other :\n**********************')