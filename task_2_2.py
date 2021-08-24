class ItemDiscount:
    def __init__(self, name, price):
        self.__name__ = name
        self.__price__ = price


class ItemDiscountReport(ItemDiscount):
    def get_parent_data(self):
        print(self.__name__, self.__price__)


child = ItemDiscountReport('sale', 10)
print(child.get_parent_data())


