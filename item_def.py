from enum import Enum

ItemType = Enum('ItemType', ['fragile, solid'])


class Item():
    id_iterator = 1
    csv_path = 'database/item.csv'

    def __init__(self, price, volume, weight, type: ItemType):
        self.id = Item.id_iterator
        Item.id_iterator += 1

        self.price = price
        self.volume = volume
        self.weight = weight
        self.type = type
