class Data:
    def __init__(self, txt):
        self.day = txt

    """Принимает  cls в качестве параметра. 
        Может получить/изменить доступ всего класса """
    @classmethod
    def get_data(cls, txt):
        data_get = []
        for i in txt.split():
            data_get.append(i)
            if i == '-':
                data_get.remove(i)
        return f'{int(data_get[0])} {int(data_get[1])} {int(data_get[2])}'

    """Не нуждается ни в каком специальном параметре, если надо прописать любой. 
        Не может получить/изменить доступ всего класса """
    @staticmethod
    def check_data(data):
        day, month, year = map(int, data.split('-'))
        return 0 < day <= 31 and 0 < month <= 12 and 0 < year <= 9999


my_list = '18 - 03  - 2001'
day_1 = Data('18 - 03  - 2001')
print(day_1.get_data('18 - 03  - 2001'))
print(day_1.check_data('18 - 03  - 2001'))
print(Data.get_data('18 - 13 - 2021'))
print(Data.check_data('18 - 13 - 2021'))
print(Data.get_data(my_list))


