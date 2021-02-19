class NotNumber(Exception):
    def __init__(self, txt):
        self.txt = txt

    def __str__(self):
        return self.txt


my_list = []
while True:
    try:
        value = input('Введите число в список:')
        if value == 'stop':
            break
        if not value.isdigit():
            raise NotNumber(f'(({value})) не число!!!')
        my_list.append(int(value))
    except NotNumber as x:
        print(x)
print(f'Результат {my_list}')
