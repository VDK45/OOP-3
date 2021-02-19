class Storage:
    def __init__(self, name: str, price: int, kol: int):
        self.name = name
        self.price = price
        self.kol = kol
        self.dic = {'kol': kol}

    def in_storage(self):
        total_kol = sum(self.dic.values())
        return f'На складе: {self.name}, цена: {self.price}руб, количество: {total_kol}'

    def __add__(self, other):
        if self.name == other.name:
            return Storage(self.name, self.price + other.price, self.kol + other.kol)

    def __str__(self):
        return f'Вместе: {self.name}, price: {self.price}rub, count: {self.kol}'




class OfficeEquip():
    def __init__(self, name, price, kol):
        self.name = name
        self.price = price
        self.kol = kol
        self.in_list = []






class Printer(OfficeEquip):
    def __init__(self, name, price, kol, color):
        super().__init__(name, price, kol)
        self.color = color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 1000:
            self.__price = 1000
        elif price > 20000:
            self.__price = 20000
        else:
            self.__price = price

    def get_price(self):
        return f'Fix price Printer {str(self.price)} rub'


class Scaner(OfficeEquip):
    def __init__(self, name, price, kol, wifi):
        super().__init__(name, price, kol)
        self.wifi = wifi

    @property
    def kol(self):
        return self.__kol

    @kol.setter
    def kol(self, kol):
        if kol < 10:
            self.__kol = 10
        elif kol > 20000:
            self.__kol = 2000
        else:
            self.__kol = kol

    def get_kol(self):
        return f'Fix kol Scaner {str(self.kol)} rub'

    def get_price(self):  # @abstractmethod needed
        pass


class Kserok(OfficeEquip):
    def __init__(self, name, price, kol, size):
        super().__init__(name, price, kol)
        self.size = size

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 1000:
            self.__price = 1000
        elif price > 20000:
            self.__price = 20000
        else:
            self.__price = price

    def get_price(self):
        return f'Fix price Kseroks {str(self.price)} rub'


aa = Kserok('Pentium', 56, 1, 6)
print(aa.get_price())
bb = Scaner('Xenon', 2030, 6, 66)
print(bb.get_kol())
cc = Printer('Cannon', 20300, 6, 66)
print(cc.get_price())

a = Storage('Printer', 4000, 10)
print(a.in_storage())
b = Storage('Printer', 5000, 5)
c = Storage('Printer', 5000, 5)
print(b.in_storage())
print(a + b + c)
print(Storage.in_storage(c))


item = Storage('Printer', 4500, 6)
print(item)
p1 = OfficeEquip('Xerok', 7000, 5)



