#line.py
def line(length, character):
    if character == "":
        print("*" * length)
    else:
        print(character[0] * length)

if __name__ == "__main__":
    line(5, "x")

#box_of_hashes
def line(length, character):
    if character == "":
        print("*" * length)
    else:
        print(character[0] * length)

def box_of_hashes(height):
    for _ in range(height):
        line(10, "#")

if __name__ == "__main__":
    box_of_hashes(5)

#square_of_hashes
def line(length, character):
    if character == "":
        print("*" * length)
    else:
        print(character[0] * length)

def square_of_hashes(size):
    for _ in range(size):
        line(size, "#")

if __name__ == "__main__":
    square_of_hashes(5)

#square
def line(length, character):
    if character == "":
        print("*" * length)
    else:
        print(character[0] * length)

def square(size, character):
    for _ in range(size):
        line(size, character)

if __name__ == "__main__":
    square(5, "x")

#triangle
def line(length, character):
    if character=="":
        print("*"*length)
    else:
        print(character[0]*length)

def triangle(size):
    for i in range(1,size+1):
        line(i,"#")

if __name__ == "__main__":
    triangle(5)

#shape
def triangle(height, char):
    total = 1
    while total <= height:
        print(char*total)
        total+=1

def rectangle(height,width,char):
    for _ in range(width):
        print(char * height)

def shape(height, char1, width, char2):
    triangle(height,char1)
    rectangle(height,width,char2)

if __name__ == "__main__":
    shape(5, "x", 2, "o")

#spruce
def spruce(height):
    n = height
    print("a spruce!")
    for i in range(n):
        spaces=(2*n-1)//2-i
        stars=2*i+1
        print(" "*spaces,end="")
        print("*"*stars)
    print(" "*((2*n-1)//2)+"*")

if __name__ == "__main__":
    spruce(3)

#greatest_number
def greatest_number(a, b, c):
    return max(a, b, c)

if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)

#same_characters
def same_chars(string, index1, index2):
    if index1 < 0 or index1 >= len(string) or index2 < 0 or index2 >= len(string):
        return False
    return string[index1] == string[index2]

if __name__ == "__main__":
    print(same_chars("coder", 1, 2))

#first_second_last
def first_word(sentence):
    return sentence.split()[0]

def second_word(sentence):
    return sentence.split()[1]

def last_word(sentence):
    return sentence.split()[-1]

if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))

#addition_and_removal
items = []

while True:
    print("The list is now", items)

    choice = input("a(d)d, (r)emove or e(x)it: ").strip().lower()

    if choice == 'd':
        if len(items) == 0:
            items.append(1) 
        else:
            items.append(items[-1] + 1)

    elif choice == 'r':
        if items:
            items.pop()  
        else:
            print("The list is already empty, nothing to remove.")

    elif choice == 'x':
        print("Bye!")
        break
    else:
        print("Invalid option. Please enter 'd', 'r', or 'x'.")

#same_word_twice
words = set()

while True:
    word = input("Word: ").strip() 

    if word in words:
        print(f"You typed in {len(words)} different words")
        break

    words.add(word)

#anagrams
def anagrams(string1, string2):
    return sorted(string1) == sorted(string2)

#palindromes
def palindromes(word):
    return word == word[::-1]

def main():
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")

main()

#sum_of_positives
def sum_of_positives(numbers):
    return sum(num for num in numbers if num > 0)

#sum_of_lists
def list_sum(list1, list2):
    return [x + y for x, y in zip(list1, list2)]

#distinct_numbers
def distinct_numbers(numbers):
    return sorted(set(numbers))

#all_longest_in_list
def all_the_longest(strings):
    max_length = max(len(s) for s in strings)
    return [s for s in strings if len(s) == max_length]

#everything_reversed
def everything_reversed(strings):
    return [s[::-1] for s in strings[::-1]]

#no_vowels_allowed
def no_vowels(s: str):
    new_string = []
    for char in s:
        if(char not in ["a","e","i","o","u"]):
            new_string.append(char)
    result = "".join(new_string)        

    return result        

#neighbours_in_list
def longest_series_of_neighbours(nums):
    if not nums:
        return 0

    max_length = 1 
    current_length = 1 

    for i in range(1, len(nums)):
        if abs(nums[i] - nums[i - 1]) == 1:
            current_length += 1  
            max_length = max(max_length, current_length)
        else:
            current_length = 1 

    return max_length

#grade_statistics
import math

def calculate_statistics():
    results = []

    while True:
        line = input("Exam points and exercises completed: ")
        if line == "":
            break
        exam_points, exercises_completed = map(int, line.split())
        results.append((exam_points, exercises_completed))

    total_points = []
    grades = []
    for exam_points, exercises_completed in results:
        exercise_points = math.floor(exercises_completed / 10)

        total = exam_points + exercise_points
        total_points.append(total)

        if exam_points < 10:
            grade = 0
        elif total <= 14:
            grade = 0
        elif total <= 17:
            grade = 1
        elif total <= 20:
            grade = 2
        elif total <= 23:
            grade = 3
        elif total <= 27:
            grade = 4
        else:
            grade = 5
        grades.append(grade)

    total_students = len(results)
    if total_students > 0:
        average_points = sum(total_points) / total_students
    else:
        average_points = 0.0

    passing_students = sum(1 for grade in grades if grade > 0)
    pass_percentage = (passing_students / total_students * 100) if total_students > 0 else 0.0

    grade_distribution = {i: 0 for i in range(6)}
    for grade in grades:
        grade_distribution[grade] += 1

    print("Statistics:")
    print(f"Points average: {average_points:.1f}")
    print(f"Pass percentage: {pass_percentage:.1f}")
    print("Grade distribution:")
    for grade in range(5, -1, -1):
        print(f"{grade}: {'*' * grade_distribution[grade]}")

calculate_statistics()

