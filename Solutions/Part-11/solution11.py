#lottery_numbers
class LotteryNumbers:
    def __init__(self, round: int, winning_numbers: list):
        self.round = round
        self.__winning_numbers = winning_numbers
 
    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.__winning_numbers])
 
    def hits_in_place(self, numbers: list):
        return [number if number in self.__winning_numbers else -1 for number in numbers]
    
#cheaper_properties
class RealProperty:
    def __init__(self, rooms: int , square_meters: int, price_per_sqm: int, description: str):
        self.rooms = rooms
        self.square_meters = square_meters
        self.price_per_sqm = price_per_sqm
        self.description = description

    def bigger(self, compared_to):
        return self.square_meters > compared_to.square_meters

    def price_difference(self, compared_to):
        difference = abs((self.price_per_sqm * self.square_meters) - (compared_to.price_per_sqm * compared_to.square_meters))
        return difference

    def more_expensive(self, compared_to):
        difference = (self.price_per_sqm * self.square_meters) - (compared_to.price_per_sqm * compared_to.square_meters)
        return difference > 0


    def __repr__(self):
        return (f'RealProperty(rooms = {self.rooms}, square_meters = {self.square_meters}, ' + 
            f'price_per_sqm = {self.price_per_sqm}, description = {self.description})')

def cheaper_properties(properties: list, reference: RealProperty):
    return [(property,property.price_difference(reference)) for property in properties if reference.more_expensive(property)]

#lengths_of_strings
def lengths(strings: list)->dict:
    return {word:len(word) for word in strings}

#most_common_words
from string import punctuation

def most_common_words(filename: str, lower_limit: int):
    with open(filename, "r") as file:
        content=file.read()
        content = content.replace("\n", " ")
        for punctuation_mark in punctuation:
            content = content.replace(punctuation_mark, "")
 
        words = content.split(" ")
        return {word: words.count(word) for word in words if words.count(word) >= lower_limit}

#balanced_brackets
def balanced_brackets(my_string: str):
    brackets = "([])"
    filtered = ""
    for char in my_string:
        filtered += char if char in brackets else ""

    if len(filtered) == 0:
        return True
    
    open_round = filtered[0] == '('
    closed_round = filtered[-1] == ")"
    open_square = filtered[0] == "["
    closed_square = filtered[-1] == "]"
    
    if not (open_round and closed_round) and not (open_square and closed_square):
        return False        
    
    return balanced_brackets(filtered[1:-1])

#greatest_node
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    node_large = root.value
    
    if root.left_child is not None:
        if greatest_node(root.left_child) > node_large:
            node_large = greatest_node(root.left_child)
    
    if root.right_child is not None:
        if greatest_node(root.right_child) > node_large:
            node_large = greatest_node(root.right_child)
    
    return node_large

#bosses_and_subordinates
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

def count_subordinates(employee: Employee):
    total=len(employee.subordinates)
    for subordinate in employee.subordinates:
        total += count_subordinates(subordinate)
    return total

#order_book
class Task:
    id=1

    def __init__(self,description,programmer,workload):
        self.description=description
        self.programmer=programmer
        self.workload=workload
        self.id=Task.id
        Task.id+=1
        self.status="NOT FINISHED"

    def mark_finished(self):
        self.status="FINISHED"

    def is_finished(self):
        if self.status=="FINISHED":
            return True
        return False
    
    def __str__(self):
        return f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {self.status}"
    
class OrderBook(Task):
    def __init__(self):
        self.book=[]
        
    def add_order(self, description, programmer, workload):
        self.book.append(Task(description, programmer, workload))

    def all_orders(self):
        return [task for task in self.book]

    def programmers(self):
        return list(set([task.programmer for task in self.book]))

    def mark_finished(self, id: int):
        for emp in self.book:
            if emp.id==id:
                emp.mark_finished()
                break
        else:
            raise ValueError

    def finished_orders(self):
        return [task for task in self.book if task.is_finished()]
    
    def unfinished_orders(self):
        return [task for task in self.book if not task.is_finished()]
    
    def status_of_programmer(self, programmer: str) -> tuple:
        finished = [task for task in self.finished_orders() if task.programmer == programmer]
        unfinished = [task for task in self.unfinished_orders() if task.programmer == programmer]
        if len(finished) == 0 and len(unfinished) == 0:
            raise ValueError
        return (len(finished), len(unfinished), sum(task.workload for task in finished), sum(task.workload for task in unfinished))
            
#order_book_application
class Task:
    id=1

    def __init__(self,description,programmer,workload):
        self.description=description
        self.programmer=programmer
        self.workload=workload
        self.id=Task.id
        Task.id+=1
        self.status="NOT FINISHED"

    def mark_finished(self):
        self.status="FINISHED"

    def is_finished(self):
        if self.status=="FINISHED":
            return True
        return False
    
    def __str__(self):
        return f"{self.description} ({self.workload} hours), programmer {self.programmer} {self.status}"
    
class OrderBook:
    def __init__(self):
        self.book=[]
        
    def add_order(self, description, programmer, workload):
        self.book.append(Task(description, programmer, workload))

    def all_orders(self):
        return [task for task in self.book]

    def programmers(self):
        return list(set([task.programmer for task in self.book]))

    def mark_finished(self, id: int):
        for emp in self.book:
            if emp.id==id:
                emp.mark_finished()
                break
        else:
            raise ValueError

    def finished_orders(self):
        return [task for task in self.book if task.is_finished()]
    
    def unfinished_orders(self):
        return [task for task in self.book if not task.is_finished()]
    
    def status_of_programmer(self, programmer: str) -> tuple:
        finished = [task for task in self.finished_orders() if task.programmer == programmer]
        unfinished = [task for task in self.unfinished_orders() if task.programmer == programmer]
        if len(finished) == 0 and len(unfinished) == 0:
            raise ValueError
        return (len(finished), len(unfinished), sum(task.workload for task in finished), sum(task.workload for task in unfinished))
            
class OrderBookApplication:
    def __init__(self):
        self.orders=OrderBook()

    def execute(self):
        print("commands:\n0 exit\n1 add order\n2 list finished tasks\n3 list unfinished tasks\n4 mark task as finished\n5 programmers\n6 status of programmer")
        while True:
            command = input("command: ")
            if command=="1":
                description = input("description: ")
                line = input("programmer and workload estimate: ")
                parts = line.split()
                if len(parts) != 2:
                    print("erroneous input")
                    continue
                programmer = parts[0]
                try:
                    workload = int(parts[1])
                except ValueError:
                    print("erroneous input")
                    continue
                self.orders.add_order(description, programmer, workload)
                print("added!")    
            elif command=="2":
                finished = self.orders.finished_orders()
                if not finished:
                    print("no finished tasks")
                else:
                    for order in finished:
                        print(order)
            elif command=="3":
                for order in self.orders.unfinished_orders():
                    print(order)
            elif command=="4":
                try:
                    id = int(input("id: "))
                    self.orders.mark_finished(id)
                    print("marked as finished")
                except ValueError:
                    print("erroneous input")
            elif command=="5":
                for programmer in self.orders.programmers():
                    print(programmer)
            elif command=="6":
                programmer = input("programmer: ")
                try:
                    finished, unfinished, finished_workload, unfinished_workload = self.orders.status_of_programmer(programmer)
                    print(f"tasks: finished {finished} not finished {unfinished}, hours: done {finished_workload} scheduled {unfinished_workload}")
                except ValueError:
                    print("erroneous input")
            elif command=="0":
                break

orders=OrderBookApplication()
orders.execute()