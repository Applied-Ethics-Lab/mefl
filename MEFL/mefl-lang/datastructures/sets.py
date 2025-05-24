# datastructures/sets.py

class CustomSet:
    def __init__(self, iterable=None):
        self._data = {}
        if iterable:
            for item in iterable:
                self.add(item)

    def add(self, item):
        self._data[item] = True

    def remove(self, item):
        if item in self._data:
            del self._data[item]

    def contains(self, item):
        return item in self._data

    def union(self, other):
        result = CustomSet()
        for item in self._data:
            result.add(item)
        for item in other._data:
            result.add(item)
        return result

    def intersection(self, other):
        result = CustomSet()
        for item in self._data:
            if other.contains(item):
                result.add(item)
        return result

    def difference(self, other):
        result = CustomSet()
        for item in self._data:
            if not other.contains(item):
                result.add(item)
        return result

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

# Example usage:
if __name__ == "__main__":
    a = CustomSet([1, 2, 3])
    b = CustomSet([2, 3, 4])
    print("Union:", list(a.union(b)))
    print("Intersection:", list(a.intersection(b)))
    print("Difference:", list(a.difference(b)))
