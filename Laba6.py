import numpy as np
from int_and_float_validation import int_input,positive_int_input
from start_info_about_me import start_info
def change_position(len_of_group,position_first_group,position_second_group,local_list):
    '''
        #функ просто міняє місцями дві групи чисел
        #якщо різниця позицій(k-p) менша ніж довжина грипу то вони місцями непоміняються(очевидно)
    :param len_of_group:
    :param position_first_group:
    :param position_second_group:
    :param same_list: example: [1,2,3,4,5,6,7,8,9]
    :return: example: [1,*8,9*,4,5,6,7,*2,3*]
    '''
    if max(position_second_group,position_first_group)-min(position_second_group,position_first_group) >= len_of_group:
        if len_of_group != 0:
            local_list[position_second_group:position_second_group + 1], \
                local_list[position_first_group:position_first_group + 1] = \
                local_list[position_first_group:position_first_group + 1], \
                local_list[position_second_group:position_second_group + 1]
            return change_position(len_of_group - 1, position_first_group + 1, position_second_group + 1, local_list)
        else:
            return local_list
        # first variant how this funk can work
        #local_list[position_second_group:position_second_group + len_of_group],local_list[position_first_group:position_first_group + len_of_group] = \
        #   local_list[position_first_group:position_first_group + len_of_group],local_list[position_second_group:position_second_group + len_of_group]
        # second variant how this funk can work
        #first_group = local_list[position_first_group:position_first_group + len_of_group]
        #second_group = local_list[position_second_group:position_second_group+len_of_group]
        #local_list[position_first_group:position_first_group+len_of_group] = second_group
        #local_list[position_second_group:position_second_group+len_of_group] = first_group
    else:
        return 'error'
def work_with_martix(row,stack):
    '''
        [
        []  - 1
        []  - 2
        []  - 3
        ]
        if sum(element[1 or 2 or 3] = min, return this sum/stack(кількість стовпців)
    :param row:
    :param stack:
    :return:
    '''
    if row>0 and stack>0:
        a = np.random.randint(-9,10,(row,stack))
        print(a)
        result = 0
        for i in range(row):
            result = min(sum(a[i]),result)
        return result/stack
    else:
        return 'error'
start_info()
while True:
    print('''
-----------------
1-open firts 
2-open second
other-exit
-----------------
        ''')
    number_of_job = input('what do you open wokr?')
    if number_of_job == '1':
        data_list = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]
        print(data_list)
        print(change_position(int_input(input('введіть довжину групи символів які хочете змінити:')),int_input(input('введіть індекс 1 групи:')),int_input(input('введіть індекс 2 групи:')),data_list))
    elif number_of_job == '2':
        print('найменше середнє арефметичне в рядках:',work_with_martix(positive_int_input(input('введіть кількість рядків:')),positive_int_input(input('введіть кількість стовпців:'))))
    else:
         exit('goodbye')
