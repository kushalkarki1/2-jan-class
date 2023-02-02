class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name

    def __eq__(self, obj):
        return self.price == obj.price

    def __add__(self, obj):
        return self.price+obj.price

    def __mul__(self, obj):
        if isinstance(obj, Product):
            return self.price * obj.price
        elif isinstance(obj, int):
            return self.price * obj

tshirt = Product("Tshirt", 2000)
jacket = Product("Jacket", 2000)
# print(tshirt+jacket)
# print(tshirt*10)


# print(all([True, True, False, True]))
# print(any([True, False, False, False]))


def append_item_to_a_list(item, a=[]):
    a.append(item)
    return a

# alist = [1, 2, 3, 4, 5]
b = append_item_to_a_list(10)
print(b)

# blist = [4, 5, 6, 7, 8]
c = append_item_to_a_list(20)
print(c)