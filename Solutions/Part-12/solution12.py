# remaining_stock
def sort_by_remaining_stock(items: list):
    return sorted(items, key=lambda item: item[2])


# climbing_route
class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"


# Write your solution herer:
def sort_by_length(routes: list):
    return sorted(routes, key=lambda item: item.length, reverse=True)


def sort_by_difficulty(routes: list):
    return sorted(routes, key=lambda item: (item.grade, item.length), reverse=True)


# climbing_areas
class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"


class ClimbingArea:
    def __init__(self, name: str):
        self.name = name
        self.__routes = []

    def add_route(self, route: ClimbingRoute):
        self.__routes.append(route)

    def routes(self):
        return len(self.__routes)

    def hardest_route(self):
        def by_difficulty(route):
            return route.grade

        routes_in_order = sorted(self.__routes, key=by_difficulty)
        # last route
        return routes_in_order[-1]

    def __str__(self):
        hardest_route = self.hardest_route()
        return f"{self.name} {self.routes()} routes, hardest {hardest_route.grade}"


def sort_by_number_of_routes(areas: list):
    return sorted(areas, key=lambda item: item.routes())


def sort_by_most_difficult(areas: list):
    return sorted(areas, key=lambda item: item.hardest_route().grade, reverse=True)


# product_search
def search(products: list, criterion: callable):
    return list(filter(criterion, products))


# even_numbers
def even_numbers(beginning: int, maximum: int):
    if beginning % 2 != 0:
        beginning += 1
    while beginning <= maximum:
        yield beginning
        beginning += 2


#prime_numbers
def prime_numbers():
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    number = 2
    while True:
        if is_prime(number):
            yield number
        number += 1

#random_words
import random

def word_generator(characters: str, length: int, amount: int):
    for _ in range(amount):
        word="".join(random.choices(characters,k=amount))
        yield word

#filtering_attempts
class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

def accepted(attempts: list):
    return list(filter(lambda student: student.grade>=1,attempts))

def attempts_with_grade(attempts: list, grade: int):
    return list(filter(lambda student: student.grade==grade,attempts))

def passed_students(attempts: list, course: str):
    return sorted(
        map(
            lambda a: a.student_name,
            filter(lambda a: a.course_name == course and a.grade > 0, attempts)
        )
    )

#credits
from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution
def sum_of_all_credits(course_list:list):
    return reduce(lambda total,item: total+item.credits,course_list,0)

def sum_of_passed_credits(course_list:list):
    return reduce(lambda total,item: total+item.credits,filter(lambda item:item.grade>=1,course_list),0)

def average(course_list:list):
    passed=len(list(filter(lambda item:item.grade>=1,course_list)))
    grades=reduce(lambda total,item: total+item.grade,filter(lambda item:item.grade>=1,course_list),0)
    return round(grades/passed,1)

#regular_expressions
import re

def is_dotw(my_string: str):
    return bool(re.fullmatch(r"Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string))

def all_vowels(my_string: str):
    return bool(re.fullmatch(r"[aeiouAEIOU]+",my_string))

def time_of_day(my_string: str):
    return bool(re.fullmatch(r"(?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d",my_string))

#
