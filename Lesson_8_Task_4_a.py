class Storage:
    items = []
    u_count = 0
    def appendDevice(self, device):
        self.items.append(device)
        Storage.u_count += 1

    def displayItems(self):
        for item in self.items:
            print(f"Устройство: {item.name}")
            print(f"Количество: {item.count}")
            print(f"Цена: {item.price}")
            print("-------------------")

    @classmethod
    def get_all_info(cls):
        return cls.items

    def __str__(self):
        return f"Товар  {self.u_count}. {self.items}"


class Device_offic:
    def __init__(self, name, price: int, count):
        self.name = name
        self.price = int(price)
        self.count = count


class Printer(Device_offic):
    def __init__(self, name, price: int, count, uniqPrinterProperty):
        super().__init__(name, price, count)
        self.uniqPrinterProperty = uniqPrinterProperty

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

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        if count < 0:
            self.__count = 1
        elif count > 200:
            self.__count = 200
        else:
            self.__count = count


class Xerox(Device_offic):
    def __init__(self, name, price: int, count, uniqXeroxProperty):
        super().__init__(name, price, count)
        self.uniqXeroxProperty = uniqXeroxProperty

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

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        if count < 0:
            self.__count = 1
        elif count > 200:
            self.__count = 200
        else:
            self.__count = count


class Scaner(Device_offic):
    def __init__(self, name, price: int, count, uniqScanerProperty):
        super().__init__(name, price, count)
        self.uniqScanerProperty = uniqScanerProperty

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

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, count):
        if count < 0:
            self.__count = 1
        elif count > 200:
            self.__count = 200
        else:
            self.__count = count


# Начало программы
storage = Storage()
up = 'нет'
us = 'нет'
ux = 'нет'
while 1:
    np = input('Введите (q) для выхода.\nМодель принтера: ')
    if np == 'q' or np == 'Q':
        break
    try:
        dp = int(input('цена: '))
        cp = int(input('Количество: '))
    except  ValueError:
        print("Ввод не верный, по умолчанию: цена - 1000, количество - 1 ")
        dp = 1
        cp = 1
    storage.appendDevice(Printer(np, dp, cp, up))
    ns = input('Введите (q) для выхода.\nМодель сканера: ')
    if ns == 'q' or ns == 'Q':
        break
    try:
        ds = int(input('цена: '))
        cs = int(input('Количество: '))
    except  ValueError:
        print("Ввод не верный, по умолчанию: цена - 1000, количество - 1 ")
        ds = 1
        cs = 1
    storage.appendDevice(Printer(ns, ds, cs, us))
    nx = input('Введите (q) для выхода.\nМодель  ксерокса: ')
    if nx == 'q' or nx == 'Q':
        break
    try:
        dx = int(input('цена: '))
        cx = int(input('Количество: '))
    except  ValueError:
        print("Ввод не верный, по умолчанию: цена - 1000, количество - 1 ")
        dx = 1
        cx = 1
    storage.appendDevice(Printer(nx, dx, cx, ux))
storage.displayItems()
print(f"На складе {storage.u_count} предмедта/ов")
