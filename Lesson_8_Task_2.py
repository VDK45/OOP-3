'''
    Класс исключений:
    не больше 100 и меньше 1000
    не менее ноля
'''

class My_error(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt
while 1:
    try:
        in_data = input('Enter number or q for quit: ')
        if in_data == 'q' or in_data == 'Q':
            break 
        elif int(in_data) > 100 and int(in_data) <= 1000:
            raise My_error('не больше 100 и меньше 1000') 
        elif int(in_data) < 0:
            raise My_error('не минус')
        elif int(in_data) == 0:
            raise My_error('не ноль') 
    except (ValueError, My_error ) as err:  # что значит err?
        print(err)
    else:
        print(f'{int(in_data)} its ok: \n100 / {int(in_data)} = {round((100 / int(in_data)), 3)}')
    
