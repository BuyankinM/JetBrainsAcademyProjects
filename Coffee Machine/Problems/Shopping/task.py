class Store:
    def __init__(self, name, category):
        self.category = category
        self.name = name

shop = Store("GAP", "clothes")
print(shop.name, shop.category)