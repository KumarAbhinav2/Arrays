"""
Implement a Hash table with get, set and remove methods
"""


class Item:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class HashTable:
    def __init__(self, size):
        self.size = size
        # every value in hash is loaded with bucket to handle collisions
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return key % self.size

    def get(self, key):
        h_val = self._hash(key)
        for item in self.table[h_val]:
            if item.key == key:
                return item.val
        raise KeyError("Item not found")

    def set(self, key, val):
        # get the index in the table to insert/replace the value
        h_val = self._hash(key)
        for item in self.table[h_val]:
            if item.key == key:
                item.val = val
                return
        new_item = Item(key, val)
        self.table[h_val].append(new_item)

    def remove(self, key):
        h_val = self._hash(key)
        for index, item in enumerate(self.table[h_val]):
            if item.key == key:
                del self.table[h_val][index]
                return
        raise KeyError("Key not found")


if __name__ == '__main__':
    hash_obj = HashTable(10)
    hash_obj.set(1, 'Abhinav')
    hash_obj.set(2, 'Ankit')
    hash_obj.set(3, 'Ankur')
    hash_obj.set(13, 'Anki')
    print(hash_obj.get(13))
