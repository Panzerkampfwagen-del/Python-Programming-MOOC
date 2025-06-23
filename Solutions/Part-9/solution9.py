#box_of_presents
class Present:
    def __init__(self,name, weight):
        self.name=name
        self.weight=weight

class Box:
    def __init__(self):
        self.presents=[]

    def add_present(self, present: Present):
        self.presents.append(present)

    def total_weight(self):
        return sum(present.weight for present in self.presents)
    
#shortest_in_room
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons=[]

    def add(self,person: Person):
        self.persons.append(person)

    def is_empty(self):
        return len(self.persons)==0

    def print_contents(self):
        heights=0
        for person in self.persons:
            heights+=person.height
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {heights} cm")
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if len(self.persons)==0:
            return None
        
        shortest=self.persons[0]
        for person in self.persons:
            if person.height < shortest.height:
                shortest=person

        return shortest
    
    def remove_shortest(self):
        shortest = self.shortest()
        if shortest:
            self.persons.remove(shortest)
            return shortest
        return None

#item_suitcase_hold
class Item:
    def __init__(self,name, weight:int):
        self.__name=name
        self.__weight=weight
    
    def weight(self):
        return self.__weight
    
    def name(self):
        return self.__name

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"

class Suitcase:
    def __init__(self, max_weight):
        self.__max_weight=max_weight
        self.__case=[]

    def add_item(self,item :Item):
        if item.weight()+self.weight()<=self.__max_weight:
            self.__case.append(item)

    def __str__(self):
        if len(self.__case)==1:
            return f"{len(self.__case)} item ({self.weight()} kg)"
        else:
            return f"{len(self.__case)} items ({self.weight()} kg)"

    def print_items(self):
        for item in self.__case:
            print(f"{item.name()} ({item.weight()} kg)")

    def weight(self):
        weight=0
        for item in self.__case:
            weight+=item.weight()
        return weight
    
    def heaviest_item(self):
        if not self.__case:
            return None
        return max(self.__case, key=lambda item: item.weight())

class CargoHold:
    def __init__(self, max_weight):
        self.__max_weight=max_weight
        self.__hold=[]

    def add_suitcase(self, suitcase: Suitcase):
        used=sum(s.weight() for s in self.__hold)
        if suitcase.weight()+used<=self.__max_weight:
            self.__hold.append(suitcase)

    def __str__(self):
        used=sum(s.weight() for s in self.__hold)
        if len(self.__hold)==1:
            return f"{len(self.__hold)} suitcase, space for {self.__max_weight-used} kg"
        else:
            return f"{len(self.__hold)} suitcases, space for {self.__max_weight-used} kg"

    def print_items(self):
        for suitcase in self.__hold:
            suitcase.print_items()