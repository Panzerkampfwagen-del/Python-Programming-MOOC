#smallest_average
def smallest_average(person1: dict, person2: dict, person3: dict):
    sums=[]
    persons=[person1,person2,person3]
    for person in persons:
        sum=0
        for value in person.values():
            if isinstance(value,int):
                sum+=value
        sums.append(sum)

    mini=sums.index(min(sums)) 
    return persons[mini]

#shopping_list
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def item(self, n: int):
        return self.products[n - 1][0]

    def amount(self, n: int):
        return self.products[n - 1][1]
    
def total_units(my_list: ShoppingList):
    total=0
    for i in range(1, my_list.number_of_items()+1):
        amount = my_list.amount(i)
        total+=amount
    return total

#decreasing_counter
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.initial_value=initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if self.value>0:
            self.value-=1

    def set_to_zero(self):
        self.value=0
    
    def reset_original_value(self):
        self.value=self.initial_value

#number_stats
class  NumberStats:
    def __init__(self):
        self.numbers=[]

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if self.count_numbers() > 0:
            return self.get_sum() / self.count_numbers()
        else:
            return 0
    
def main():
    all_numbers = NumberStats()
    even_numbers = NumberStats()
    odd_numbers = NumberStats()

    print("Please type in integer numbers:")
    while True:
        number = int(input())
        if number == -1:
            break
        all_numbers.add_number(number)

        if number % 2 == 0:
            even_numbers.add_number(number)
        else:
            odd_numbers.add_number(number)

    print(f"Sum of numbers: {all_numbers.get_sum()}")
    print(f"Mean of numbers: {all_numbers.average()}")
    print(f"Sum of even numbers: {even_numbers.get_sum()}")
    print(f"Sum of odd numbers: {odd_numbers.get_sum()}")

main()

#stopwatch
class Stopwatch:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def tick(self):
        self.seconds+=1
        if self.seconds>59:
            self.minutes+=1
            self.seconds=0

        if self.minutes > 59:
            self.seconds=0
            self.minutes=0
        
    def __str__(self):
        return f"{self.minutes:02}:{self.seconds:02}"

#series
class Series:
    def __init__(self,title:str,season:int,genre:list):
        self.title=title
        self.season=season
        self.genre=genre
        self.rating=[]

    def __str__(self):
        if len(self.rating)==0:
            return f"{self.title} ({self.season} seasons) \ngenres: {', '.join(self.genre)} \nno ratings"
        else:
            return f"{self.title} ({self.season} seasons) \ngenres: {', '.join(self.genre)} \n{len(self.rating)} ratings, average {self.average():.1f} points"
    
    def rate(self,rating: int):
        self.rating.append(rating)

    def average(self):
        return sum(self.rating)/len(self.rating) if self.rating else 0.0
    
def minimum_grade(rating: float, series_list: list):
        select=[]
        for series in series_list:
            if series.average() >= rating:
                select.append(series)
        return select

def includes_genre(genre: str, series_list: list):
        select=[]
        for series in series_list:
            if genre in series.genre:
                select.append(series)
        return select