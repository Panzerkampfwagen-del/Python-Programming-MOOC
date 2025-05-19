#fruit_market
def read_fruits():
    fruits_dict = {}
    
    with open("fruits.csv", "r") as file:
        for line in file:
            fruit, price = line.strip().split(";")
            fruits_dict[fruit] = float(price)
    
    return fruits_dict

#matrix
def matrix_sum():
    msum=0
    with open("matrix.txt","r") as file:
        for line in file:
            line= map(int, line.strip().split(","))
            msum+=sum(line)
    return msum


def matrix_max():
    Max=0
    with open("matrix.txt","r") as file:
        for line in file:
            line= map(int, line.strip().split(","))
            Max=max(max(line),Max)
    return Max


def row_sums():
    rsum=[]
    with open("matrix.txt","r") as file:
        for line in file:
            line= map(int, line.strip().split(","))
            rsum.append(sum(line))
    return rsum

#course_grading_part_1
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")

course={}
with open(exercise_data) as file:
    for line in file:
        line=line.strip().split(";")
        if line[0]=="id":
            continue
        else:
            course[line[0]]=sum(map(int,line[1:]))

Name={}
with open(student_info) as file:
    for line in file:
        line=line.strip().split(";")
        if line[0]=="id":
            continue
        else:
            Name[line[0]]=line[1]+" "+line[2]

pic=[]
with open(student_info) as file:
    for line in file:
        line=line.strip().split(";")
        if line[0]=="id":
            continue
        else:
            pic.append(line[0])

for no in pic:           
    print(f"{Name[no]} {course[no]}")

#course_grading_part_2
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data=input("Exam marks: ")

course={}
with open(exercise_data) as file:
    for line in file:
        line=line.strip().split(";")
        if line[0]=="id":
            continue
        else:
            point=sum(map(int,line[1:])) // 4
            course[line[0]]=point

Name={}
pic=[]
with open(student_info) as file:
    for line in file:
        line=line.strip().split(";")
        if line[0]=="id":
            continue
        else:
            Name[line[0]]=line[1]+" "+line[2]
            pic.append(line[0])

point={}
with open(exam_data) as file:
    for line in file:
        line=line.strip().split(";")
        if line[0]=="id":
            continue
        else:
            point[line[0]]=sum(map(int,line[1:]))

total={}
for no in pic:
    total[no]=point[no]+course[no]

grade={}
for no,marks in total.items():
    if marks < 15:
        grade[no] = 0
    elif marks <= 17:
        grade[no] = 1
    elif marks <= 20:
        grade[no] = 2
    elif marks <= 23:
        grade[no] = 3
    elif marks <= 27:
        grade[no] = 4
    elif marks > 27:
        grade[no] = 5

for no in pic:           
    print(f"{Name[no]} {grade[no]}")

#course_grading_part_3
student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data=input("Exam marks: ")

course={}
exercises={}
with open(exercise_data) as file:
    for line in file:
        line=line.strip().split(";")
        if line[0]=="id":
            continue
        else:
            point=sum(map(int,line[1:]))
            course[line[0]]=point//4
            exercises[line[0]]=point

Name={}
pic=[]
with open(student_info) as file:
    for line in file:
        line=line.strip().split(";")
        if line[0]=="id":
            continue
        else:
            Name[line[0]]=line[1]+" "+line[2]
            pic.append(line[0])

point={}
with open(exam_data) as file:
    for line in file:
        line=line.strip().split(";")
        if line[0]=="id":
            continue
        else:
            point[line[0]]=sum(map(int,line[1:]))

total={}
for no in pic:
    total[no]=point[no]+course[no]

grade={}
for no,marks in total.items():
    if marks < 15:
        grade[no] = 0
    elif marks <= 17:
        grade[no] = 1
    elif marks <= 20:
        grade[no] = 2
    elif marks <= 23:
        grade[no] = 3
    elif marks <= 27:
        grade[no] = 4
    elif marks > 27:
        grade[no] = 5

print("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade")
for no in pic:           
    print(f"{Name[no]:30}{exercises[no]:<10}{course[no]:<10}{point[no]:<10}{total[no]:<10}{grade[no]:<10}")

#spellchecker
word=input("please type some text: ")

words=[]
with open("wordlist.txt") as file:
    for line in file:
        line=line.strip()
        words.append(line)

word=word.split()
for i,text in enumerate(word):
    if i==0:
        new=text.lower()
        if new not in words:
            word[i]=f"*{text}*"
    elif text not in words:
        word[i]=f"*{text}*"

print(" ".join(word))

#recipe_search
# Write your solution here
def search_by_name(filename: str, word: str) -> list:
    complete=[]
    with open(filename) as file:
        for line in file:
            complete.append(line.strip())

    name=[]
    name.append(complete[0])
    for i,text in enumerate(complete):
        if text=="":
            name.append(complete[i+1])
               

    found=[]
    for text in name:
        if word.lower() in text.lower():
            found.append(text)

    return found

def search_by_time(filename: str, prep_time: int) -> list:
    recipe_dict={}
    complete=[]
    with open(filename) as file:
        for line in file:
            complete.append(line.strip())

    recipe_dict[complete[0]]=int(complete[1])
    for i,text in enumerate(complete):
        if text=="":
            recipe_dict[complete[i+1]]=int(complete[i+2])

    found=[]
    for name,time in recipe_dict.items():
        if time<=prep_time:
            found.append(f"{name}, preparation time {time} min")

    return found

def search_by_ingredient(filename: str, ingredient: str) -> list:
    prep_time = {}
    recipe = {}
    ingredients = []
    recipe_name = ""
    counter = 0

    with open(filename) as new_file:
        for line in new_file:
            line = line.strip()
            if line.isnumeric():
                prep_time[recipe_name] = int(line)
                counter = 1
            elif counter == 1:
                if line == "":
                    recipe[recipe_name] = ingredients
                    ingredients = []
                    counter = 0
                    continue
                ingredients.append(line.lower())
            else:
                recipe_name = line
                counter = 0
        if recipe_name and ingredients:
            recipe[recipe_name] = ingredients

    found = []
    for recipe_name, items in recipe.items():
        for item in items:
            if ingredient.lower() in item:
                found.append(f"{recipe_name}, preparation time {prep_time[recipe_name]} min")
                break

    return found

#city_bikes
import math

def get_station_data(filename: str) -> dict:
    coords={}
    with open(filename) as file:
        for line in file:
            line=line.strip().split(";")
            if line[0]=="Longitude":
                continue
            else:
                coords[line[3]]=(float(line[0]),float(line[1]))

    return coords

def distance(stations: dict, station1: str, station2: str) -> float:
    coord=[]
    for station,coords in stations.items():
        if station==station1 or station==station2:
            coord.append(coords)

    x_km = (coord[0][0]-coord[1][0])*55.26
    y_km = (coord[0][1]-coord[1][1])*111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations: dict)-> tuple:
    cities=[]
    for city in stations:
        cities.append(city)

    dis={}
    for i in range(len(cities)):
        for j in range(i+1,len(cities)):
            dis[(cities[i], cities[j])]=distance(stations, cities[i], cities[j])

    city1,city2=None,None
    max_dis=0
    for city,distances in dis.items():
        if distances>max_dis:
            max_dis=distances
            city1,city2 = city

    return (city1,city2,max_dis)

#diary
while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function=input("1 - add an entry, 2 - read entries, 0 - quit")

    if function=="1":
        with open('diary.txt',"a") as file:
            diary_entry=input("Diary entry: ")
            file.write(diary_entry+"\n")
            print("Diary saved")
    
    if function=="2":
        with open('diary.txt',"r") as file:
            print("Entries:")
            for line in file:
                print(line.strip())
        
    if function == "0":
        print("Bye now!")  
        break

#filtering_file_contents
def filter_solutions():
    correct=[]
    incorrect=[]
    with open("solutions.csv") as file:
        for line in file:
            line=line.strip().split(";")
            if eval(line[1])==int(line[2]):
                correct.append(f"{line[0]};{line[1]};{line[2]}")
            else:
                incorrect.append(f"{line[0]};{line[1]};{line[2]}")
                
    with open("correct.csv","w") as file:
        for child in correct:
            file.write(child+"\n")

    with open("incorrect.csv","w") as file:
        for child in incorrect:
            file.write(child+"\n")

#course_grading_part_4
def title_header(filename: str):
    course = []
    with open(filename) as course_detail:
        for line in course_detail:
            parts = line.split(":")
            course.append(parts[1].strip())
    
    title = course[0] + ", " + course[1] + " credits" + "\n"
    border = (len(title)-1) * "=" + "\n"
    header = f'{"name":<30}{"exec_nbr":<10}{"exec_pts.":<10}{"exm_pts.":<10}{"tot_pts.":<10}{"grade":<10}' + "\n"
    return title, border, header

def grader(points: int):
    grades = [0, 1, 2, 3, 4, 5]
    limits = [0, 15, 18, 21, 24, 28]
    for limit in limits[::-1]:
        if points >= limit:
            grade = grades[limits.index(limit)]
            break
        else:
            continue
    return grade


def to_point(exercises: list):
    return sum(exercises) // 4


def report(students: dict, exercises: dict, exams: dict):
    line = ""
    csv = ""
    for pic, name in students.items():
        exercises_points = to_point(exercises[pic])
        total_exercises = sum(exercises[pic])
        exam_points = sum(exams[pic])
        total_points = exercises_points + exam_points
        grade = grader(total_points)
        line += f'{name:30}{total_exercises:<10}{exercises_points:<10}{exam_points:<10}{total_points:<10}{grade:<10}\n'
        csv += f'{pic};{name};{grade}\n'
    return line, csv


student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_data = input("Exam points: ")
course_info = input("Course information: ")


students = {}
with open(student_info) as new_file:
    for line in new_file:
        line = line.strip()
        parts = line.split(";")
        if parts[0] == "id":
            continue
        students[parts[0]] = parts[1] + " " + parts[2]

exercises = {}
with open(exercise_data) as new_file:
    for line in new_file:
        parts = line.split(";")
        if parts[0] == "id":
            continue
        exercises[parts[0]] = []
        for part in parts[1:]:
            part = part.strip()
            part = int(part)
            exercises[parts[0]].append(part)

exams = {}
with open(exam_data) as new_file:
    for line in new_file:
            parts = line.split(";")
            if parts[0] == "id":
                continue
            exams[parts[0]] = []
            for part in parts[1:]:
                part = part.strip()
                part = int(part)
                exams[parts[0]].append(part)

with open("results.txt", "w") as text_result, open("results.csv","w") as csv_result:   
    title, border, header = title_header(course_info)
    text_result.write(title)
    text_result.write(border)
    text_result.write(header)
    line, csv = report(students, exercises, exams)
    text_result.write(line)
    csv_result.write(csv)

#word_search
import re

def find_words(search_term: str)->list:
    match=[]
    if "." in search_term:
        return dot(search_term)
    elif "*" in search_term:
        return asterisk(search_term) 
    else:
        with open("words.txt") as file:
            for line in file:
                word=line.strip()
                if search_term==word:
                    match.append(word)

    return match

def asterisk(search_term: str) -> list:
    match=[]
    search_term=search_term.replace('*', '.*')
    with open("words.txt") as file:
        for line in file:
            line=line.strip()
            if re.fullmatch(search_term,line):
                match.append(line)

    return match

def dot(search_term: str) -> list:
    match=[]
    with open("words.txt") as file:
        for line in file:
            line=line.strip()
            if re.fullmatch(search_term,line):
                match.append(line)

    return match
    
#dictionary_file
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function=input("function")
    if function=="1":
        fin_dict={}
        finnish=input("The word in Finnish: ")
        english=input("The word in English: ")
        fin_dict[finnish]=english
        with open("dictionary.txt","a") as file:
            file.write(f"{finnish} - {fin_dict[finnish]}\n")
            print("Dictionary entry added")
        continue

    elif function=="2":
        search=input("Search term: ")
        with open("dictionary.txt") as file:
            for line in file:
                line=line.strip().split(" - ")
                if search in line[0] or search in line[1]:
                    print(f"{line[0]} - {line[1]}")
        continue

    elif function=="3":
        print("Bye!")
        break

#read_input
def read_input(input_string: str, lower_bound: int, upper_bound: int):
    while True:
        try:
            number = int(input(input_string))
            if number > lower_bound and number < upper_bound:
                return number
        except ValueError:
            pass
        print(f"You must type in an integer between {lower_bound} and {upper_bound}")

#incorrect_lottery_numbers
import re

def filter_incorrect():
    correct={}
    
    with open("lottery_numbers.csv") as file:
        for line in file:
            line=line.strip().split(";")
            name=line[0].strip()
            numbers = line[1].split(",")

            if not re.match(r'^week \d+$', name):
                continue    
        
            try:
                nums=[int(x) for x in numbers]
            except ValueError:
                continue

            if (len(nums)==7 and all(1<=x<=39 for x in nums) and len(set(nums))==len(nums)):
                correct[name]=nums

    with open("correct_numbers.csv","w") as file:
        for key,values in correct.items():
            file.write(f"{key};{",".join(map(str,values))}\n")

#
    

