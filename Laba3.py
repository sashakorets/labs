from start_info_about_me import start_info

def RemoveSameSimvol(text,siparator,first_simvol_of_word,star_index,end_index):
    '''
        func delete range(:param star_index,:param end_index) in everyone word in :param text, if word[0] == :param first_simvol_of_word
    :param text: (str) input data
    :param siparator:
    :param first_simvol_of_word: (str) if world[0] == this simvol
    :param star_index: {we delete characters in each word in range(start)index,end_index)
    :param end_index:  {we delete characters in each word in range(start)index,end_index)
    :return: improved text (str)
    '''
    data_list = text.split(siparator)
    for index, word in enumerate(data_list[0:len(data_list):1]):
        # print(index, word)
        if word[0].lower() == first_simvol_of_word and len(word) >= max(end_index,star_index):
            word = word[min(end_index,star_index):max(end_index,star_index)]
            data_list[index] = word
        elif word[0].lower() == first_simvol_of_word and len(word) < max(end_index,star_index) and len(word) > min(end_index,star_index):
            word = word[min(end_index,star_index):]
            data_list[index] = word
        elif word[0].lower() == first_simvol_of_word and len(word) <= min(end_index, star_index):
            word = ''
            data_list[index] = word
        else:
            continue
    return (','.join(data_list))

start_info()

print('''------------------
task condision
Видалити певні 
символи від 'a' до 
'b' зі слів,
що починаються 
на 'деякий символ'
------------------''')

while True:
    loop_question=input('''***********
1-lets go
other-exit
***********
lets go or no?
''')
    if loop_question=='1':
        print(RemoveSameSimvol(input('input same text:'),' ','t',2,4))
    else :
        exit('goodbye')