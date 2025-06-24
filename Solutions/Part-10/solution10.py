#laptop_computer
class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property
    def model(self):
        return self.__model

    @property
    def speed(self):
        return self.__speed

class LaptopComputer(Computer):
    def __init__(self,model,speed, weight:int):
        super().__init__(model,speed)
        self.weight=weight

    def __str__(self):
        return f"{super().model}, {super().speed} MHz, {self.weight} kg"
    
#game_museum
class ComputerGame:
    def __init__(self, name: str, publisher: str, year: int):
        self.name = name
        self.publisher = publisher
        self.year = year

class GameWarehouse:
    def __init__(self):
        self.__games = []

    def add_game(self, game: ComputerGame):
        self.__games.append(game)

    def list_games(self):
        return self.__games
    
class GameMuseum(GameWarehouse):
    def __init__(self):
        super().__init__()

    def list_games(self):
        return [game for game in super().list_games() if game.year<1990]

#word_game
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            winner = self.round_winner(answer1, answer2)

            if winner == 1:
                self.wins1 += 1
                print("player 1 won")
            elif winner == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                print("tie")

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        if len(player1_word)>len(player2_word):
            return 1
        elif len(player1_word)<len(player2_word):
            return 2
        else:
            return 0
        
class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        def count_vowels(word):
            return sum(1 for char in word.lower() if char in "aeiou")

        v1 = count_vowels(player1_word)
        v2 = count_vowels(player2_word)

        if v1 > v2:
            return 1
        elif v2 > v1:
            return 2
        else:
            return 0 
    
class RockPaperScissors(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)

    def round_winner(self, player1_word: str, player2_word: str):
        allowed = ["rock", "paper", "scissors"]

        p1_valid = player1_word in allowed
        p2_valid = player2_word in allowed

        if not p1_valid and not p2_valid:
            return 0
        if not p1_valid:
            return 2
        if not p2_valid:
            return 1

        if player1_word == player2_word:
            return 0

        if (player1_word == "rock" and player2_word == "scissors") or \
        (player1_word == "paper" and player2_word == "rock") or \
        (player1_word == "scissors" and player2_word == "paper"):
            return 1
        else:
            return 2
        
#supergroup
class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'

class SuperGroup(SuperHero):
    def __init__(self,name:str,location:str):
        self._name=name
        self._location=location
        self._members=[]

    @property
    def name(self):
        return self._name
    
    @property
    def location(self):
        return self._location
    
    def add_member(self,hero: SuperHero):
        self._members.append(hero)

    def print_group(self):
        print(f"{self.name}, {self.location} \nMembers:")
        for person in self._members:
            print(f"{person.name}, superpowers: {person.superpowers}")

#secret_magic_potion
class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")


class SecretMagicPotion(MagicPotion):
    def __init__(self, name,password:str):
        super().__init__(name)
        self._password=password

    def add_ingredient(self,ingredient: str, amount: float, password: str):
        if password!=self._password:
            raise ValueError
        self._ingredients.append((ingredient,amount))

    def print_recipe(self,password: str):
        if password!=self._password:
            raise ValueError
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")

#money
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02} eur"
    
    def __eq__(self, another):
        return ((self._euros==another._euros) and (self._cents==another._cents))
    
    def __lt__(self,another):
        if self._euros==another._euros:
            return self._cents<another._cents
        return self._euros<another._euros
    
    def __gt__(self,another):
        if self._euros==another._euros:
            return self._cents>another._cents
        return self._euros>another._euros
    
    def __ne__(self,another):
        if self._euros==another._euros:
            return self._cents!=another._cents
        return self._euros!=another._euros
    
    def __add__(self,another):
        new=Money(0,0)
        new._euros=self._euros+another._euros
        new._cents=self._cents+another._cents
        if new._cents>=100:
            new._euros += new._cents // 100
            new._cents = new._cents % 100
        return new
    
    def __sub__(self,another):
        self_total_cents = self._euros * 100 + self._cents
        other_total_cents = another._euros * 100 + another._cents

        if self_total_cents < other_total_cents:
            raise ValueError

        result_cents = self_total_cents - other_total_cents
        euros = result_cents // 100
        cents = result_cents % 100

        return Money(euros, cents)
    
#simple_date
class SimpleDate:
    def __init__(self,day,month,year):
        self.day=day
        self.month=month
        self.year=year

    def __eq__(self,another):
        return (self.day==another.day) and (self.month==another.month) and \
        (self.year==another.year)
    
    def __ne__(self,another):
        return not self.__eq__(another)
    
    def __lt__(self,another):
        if self.year < another.year:
            return True
        if self.year == another.year and self.month < another.month:
            return True
        if self.year == another.year and self.month == another.month and \
        self.day < another.day:
            return True
        return False

    def __gt__(self,another):
        return not self.__lt__(another)
    
    def __add__(self,day):
        total_days = self.year * 360 + self.month * 30 + self.day
        total_days += day

        new_year = total_days // 360
        total_days %= 360
        new_month = total_days // 30
        new_day = total_days % 30

        if new_day == 0:
            new_day = 30
            if new_month == 0:
                new_month = 12
                new_year -= 1
            else:
                new_month -= 1

        return SimpleDate(new_day, new_month, new_year)
    
    def __sub__(self,another):
        self_days = self.year * 360 + self.month * 30 + self.day
        other_days = another.year * 360 + another.month * 30 + another.day
        return abs(self_days - other_days)
    
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
    
#iterable_shopping_list
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def product(self, n: int):
        return self.products[n - 1][0]

    def number(self, n: int):
        return self.products[n - 1][1]
    
    def __iter__(self):
        self.n=0
        return self
    
    def __next__(self):
        if self.n<len(self.products):
            item=self.product(self.n+1)
            number=self.number(self.n+1)
            self.n+=1
            return (item,number)
        else:
            raise StopIteration
        
#phone_book_v1
class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = []

        self.__persons[name].append(number)

    def get_numbers(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]
    
    def get_name(self, number:str):
        for name, numbers in self.__persons.items():
            if number in numbers:
                return name
        return None    
        
    def all_entries(self):
        return self.__persons

class FileHandler():
    def __init__(self, filename):
        self.__filename = filename

    def load_file(self):
        names = {}
        with open(self.__filename) as f:
            for line in f:
                parts = line.strip().split(';')
                name, *numbers = parts
                names[name] = numbers
        return names

    def save_file(self, phonebook: dict):
        with open(self.__filename, "w") as f:
            for name, numbers in phonebook.items():
                line = [name] + numbers
                f.write(";".join(line) + "\n")
                
class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("phonebook.txt")

        for name, numbers in self.__filehandler.load_file().items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add entry")
        print("2 search")
        print("3 search by number")

    def add_entry(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def search(self):
        name = input("name: ")
        numbers = self.__phonebook.get_numbers(name)
        if numbers == None:
            print("number unknown")
            return
        for number in numbers:
            print(number)

    def search_name(self):
        number=input("number: ")
        name=self.__phonebook.get_name(number)
        if name == None:
            print("unknown number")
            return
        print(name)

    def exit(self):
        self.__filehandler.save_file(self.__phonebook.all_entries())

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.search_name()
            else:
                self.help()

application = PhoneBookApplication()
application.execute()

#phone_book_v2
class Person:
    def __init__(self,name):
        self.__name=name
        self.__numbers=[]
        self.__address=None

    def add_number(self,number):
        if number not in self.__numbers:
            self.__numbers.append(number)

    def add_address(self,address):
        self.__address=address

    def name(self):
        return self.__name

    def numbers(self):
        return self.__numbers
    
    def address(self):
        return self.__address

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: str):
        if not name in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def get_entry(self, name: str):
        if not name in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons
    
    def add_address(self, name:str, address: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)        
        self.__persons[name].add_address(address)

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        entry = self.__phonebook.get_entry(name)
        if entry is None:
            print("number unknown")
            print("address unknown")
            return
        if len(entry.numbers()) == 0:
            print("number unknown") 
        else:
            for number in entry.numbers():
                print(number)
        if entry.address() is None:
            print("address unknown")
        else:
            print(entry.address())       

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()

application = PhoneBookApplication()
application.execute()

#course_records
class Course:
    def __init__(self):
        self.__course={}

    def add_course(self,course:str,grade:int,credits:int):
        if course not in self.__course:
            self.__course[course]=[grade,credits]

        elif grade > self.__course[course][0]:
            self.__course[course]=[grade,credits]

        else:
            pass

    def get_course_data(self,course:str):
        if course not in self.__course:
            print("no entry for this course")

        else:
            print(f"{course} ({self.__course[course][1]} cr) grade {self.__course[course][0]}")
            
    def credits(self):
        return sum(self.__course[course][1] for course in self.__course)
    
    def grade(self):
        return sum(self.__course[course][0] for course in self.__course)
            
    def statistics(self):
        print(f"{len(self.__course)} completed courses, a total of {self.credits()} credits")
        print(f"mean {(self.grade()/len(self.__course)):.1f}\ngrade distribution:")

        counter={}
        for course in self.__course:
            grade = self.__course[course][0]

            if grade not in counter:
                counter[grade] = 0
            counter[grade] += 1

        print(f"5: {'x'*counter.get(5,0)}\n4: {'x'*counter.get(4,0)}\n3: {'x'*counter.get(3,0)}\n2: {'x'*counter.get(2,0)}\n1: {'x'*counter.get(1,0)}")

    def execute(self):
        print("command:\n1 add course\n2 get course data\n3 statistics\n0 exit")
        while True:
            command=input("command: ")
            if command=="1":
                course=input("course: ")
                grade=int(input("grade: "))
                credits=int(input("credits: "))
                self.add_course(course,grade,credits)

            elif command=="2":
                course=input("course: ")
                self.get_course_data(course)

            elif command=="3":
                self.statistics()

            elif command=="0":
                break
            
course=Course()
course.execute()