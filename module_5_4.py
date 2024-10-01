class House:
    houses_hystory = []
    instance = None

    def __new__(cls, args, kwargs):
        if cls.instance is None:
            cls.instanse = super().__new__(cls)
            cls.houses_hystory.append(args)
        return cls.instanse

    def __del__(self):
        print( f'{self.name} снесён, но он останется в истории')

        return

    def __init__(self , name , number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'  Название:  " {self.name}" , кол-во этажей: "{self.number_of_floors}" '

    def __eq__(self, other):
        if isinstance(other , House):
            return self.number_of_floors == other.number_of_floors
        else:
            return ('!!!невозможное сравнение!!!')

    def __lt__(self, other):
        if isinstance(other , House):
            return  self.number_of_floors < other.number_of_floors
        else:
            return ('!!!невозможное сравнение!!!')

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return ('!!!невозможное сравнение!!!')

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return ('!!!невозможное сравнение!!!')

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return ('!!!невозможное сравнение!!!')

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return ('!!!невозможное сравнение!!!')

    def __add__(self, other):
        if isinstance(other , int):
            self.number_of_floors = self.number_of_floors + other
            return self
        else:
            return ('???????')

    def __iadd__(self, other):
        if isinstance(other , int):
            self.number_of_floors += other
            return self
        else:
            return ('???????')

    def __radd__(self, other):
        if isinstance(other , int):
            self.number_of_floors = other + self.number_of_floors
            return self
        else:
            return ('???????')



    def go_to(self , floor):
        if int(floor) > self.number_of_floors:
            print(f'Этаж {floor} не существует в {self.name}')
        if int(floor) in range(1 , int(self.number_of_floors)):
            for i in range(1 , floor+1):
                print(i)
        if int(floor) < -1:
            print(f'Этаж {floor} не существует в {self.name}')
        if floor == 0:
            print("зачем???")


#h1 = House('ЖК Эльбрус', 10)
#h2 = House('ЖК Акация', 20)

#print(h1)
#print(h2)

#print(h1 == h2) # __eq__

#h1 = h1 + 10 # __add__
#print(h1)
#print(h1 == h2)

#h1 += 10 # __iadd__
#print(h1)

#h2 = 10 + h2 # __radd__
#print(h2)

#print(h1 > h2) # __gt__
#print(h1 >= h2) # __ge__
#print(h1 < h2) # __lt__
#print(h1 <= h2) # __le__
#print(h1 != h2) # __ne__


h1 = House('ЖК Эльбрус', 10)
print(House.houses_hystory)

h2 = House('ЖК Акация', 20)
print(House.houses_hystory)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_hystory)

del h2
del h3

print(House.houses_hystory)