

class Node:
    def __init__(self, value):
        self.children = []
        self.value = value

    def add_child(self, value):
        self.children.append(Node(value))

    def __repr__(self):
        classname = type(self).__name__
        return (f'{classname}({self.value!r}, {self.children})' if self.children else
                f'{classname}({self.value!r})')

    def print_stat(self):
        print(self.children)
        print(self.value)


class CategoryTree:
    def __init__(self):
        self.continents = {}  # Dictionary mapping continents to countries.

    def addCateogry(self, subCategory, parent=None):
        if not parent:  # Adding a continent?
            continent = subCategory
            self.continents[continent] = Node(continent)
        else:  # Adding a country to a continent.
            continent = self.continents.get(parent, None)
            print(self.continents)
            if not continent:
                raise KeyError(f'No continent named {parent} exists')
            continent.add_child(subCategory)

    def getCategory(self, parent):
        continent = self.continents.get(parent, None)
        if not continent:
            raise KeyError(f'No continent named {parent} exists')
        return continent.children
