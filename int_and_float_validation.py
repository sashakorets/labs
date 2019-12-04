import re

def int_input(text):
    '''
    :param text: (str)
        123132 - True
        qweqwe 123213 - False
        2312312asd . - False
    :return: (int)
    '''
    pattern_int = r"^[-\d]\d*$"
    user_input = text
    while not re.match(pattern_int, user_input):
        user_input = input("Enter int:")
    return int(user_input)

def float_input(text):
    '''
    :param text: (str)
        123132.232 - True
        qweqwe 123213 - False
        2312312asd . - False
    :return: (float)
    '''
    pattern_float = r"[-\d]\d*\.?\d*$"
    user_input = text
    while not re.match(pattern_float, user_input):
        user_input = input("Enter float:")
    return float(user_input)

def positive_int_input(text):
    '''
    :param text: (str)
        123132 - True
        qweqwe 123213 - False
        2312312asd . - False
    :return: (int)
    '''
    pattern_int = r"^[\d]\d*$"
    user_input = text
    while not re.match(pattern_int, user_input):
        user_input = input("Enter int:")
    return int(user_input)