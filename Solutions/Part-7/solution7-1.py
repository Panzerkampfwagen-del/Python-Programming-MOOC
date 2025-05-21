#special_characters
import string

def separate_characters(my_string: str)->tuple:
    part1=[]
    part2=[]
    part3=[]
    for character in my_string:
        if character in string.ascii_letters:
            part1.append(character)
        elif character in string.punctuation:
            part2.append(character)
        else:
            part3.append(character)

    return(("".join(part1),"".join(part2),"".join(part3)))  

#password_generator_part_2
import random
import string

def generate_strong_password(length:int, farg:bool, sarg:bool) -> str:
    subset=string.ascii_lowercase
    passw=[random.choice(string.ascii_lowercase)]
    if farg==True:
        subset+=string.digits
        passw.append(random.choice(string.digits))

    if sarg==True:
        subset+="!?=+-()#"
        passw.append(random.choice("!?=+-()#"))

    rem_length=length-len(passw)
    passw+=random.choices(subset,k=rem_length)

    random.shuffle(passw)
    return "".join(passw)

#dice_roller
import random

def roll(die: str) -> int:
    dieA=[3, 3, 3, 3, 3, 6]
    dieB=[2, 2, 2, 5, 5, 5]
    dieC=[1, 4, 4, 4, 4, 4]
    if die=="A":
        return random.choice(dieA)
    elif die=="B":
        return random.choice(dieB)
    else:
        return random.choice(dieC)

def play(die1: str, die2: str, times: int)->tuple:
    die_1=0
    die_2=0
    tie=0
    for i in range(times):
        roll_1=roll(die1)
        roll_2=roll(die2)
        if roll_1>roll_2:
            die_1+=1
        elif roll_2>roll_1:
            die_2+=1
        else:
            tie+=1

    return (die_1,die_2,tie)
        
#random_words
import random

def words(n: int, beginning: str)->list:
    words=[]
    with open("words.txt") as file:
        for line in file:
            line=line.strip()
            if line.startswith(beginning):
                words.append(line)

    if len(words)<n:
        raise ValueError
    
    return random.sample(words, k=n)

#how_old
import datetime

day=int(input("Day: "))
month=int(input("Month: "))
year=int(input("Year: "))

birth_date=datetime.date(year,month,day)
millenium=datetime.date(1999,12,31)

age=millenium-birth_date

if age.days > 0:
        print(f"You were {age.days} days old on the eve of the new millennium.")
else:
        print(f"You weren't born yet on the eve of the new millennium.")

#valid_pic
import datetime

def is_it_valid(pic: str)->bool:
    if len(pic) != 11:
        return False
    
    if pic[6] not in "+-A":
        return False
    
    if pic[6]=="-":
        century=1900
    elif pic[6]=="+":
        century=1800
    else:
        century=2000

    try:
        day = int(pic[0:2])
        month = int(pic[2:4])
        year = int(pic[4:6])
        full_year = century + year
        date=datetime.date(full_year,month,day)
    except ValueError:
        return False
    
    check="0123456789ABCDEFHJKLMNPRSTUVWXY"
    number=int("".join(pic[:6]+pic[7:10]))
    number=number%31
    if pic[10]==check[number]:
        pass
    else:
        return False
    
    return True

#screen_time
import datetime

filename=input("Filename: ")
start=input("Starting date: ")
start_date=datetime.datetime.strptime(start, "%d.%m.%Y")
days=int(input("How many days: "))

print("Please type in screen time in minutes on each day (TV computer mobile):")

info=[]

for i in range(days):
    time=start_date+datetime.timedelta(days=i)
    entry=input(f"Screen time {time.strftime("%d.%m.%Y")}: ")
    info.append((time,entry))

total_minutes=0
for _, value in info:
    tv, comp,mob = map(int,value.split())
    total_minutes+=tv+comp+mob

avg=total_minutes/days

with open(filename,"w") as file:
    file.write(f"Time period: {start_date.strftime('%d.%m.%Y')}-{(start_date + datetime.timedelta(days=days-1)).strftime('%d.%m.%Y')}\n")
    file.write(f"Total minutes: {total_minutes}\n")
    file.write(f"Average minutes: {avg}\n")

    for date,entry in info:
        tv, comp, mob = entry.split()
        file.write(f"{date.strftime('%d.%m.%Y')}: {tv}/{comp}/{mob}\n")

print(f"Data stored in file {filename}.txt")

#json_files
import json

def print_persons(filename: str)->None:
    with open(filename) as file:
        contents=file.read()

    contents=json.loads(contents)

    for dic in contents:
        print(f"{dic['name']} {dic['age']} years ({", ".join(dic['hobbies'])})")

#course_statistics
import urllib.request
import json
import math

def retrieve_all()->list:
    url=urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    json_format=url.read()
    contents=json.loads(json_format)

    retrieved=[]

    for dic in contents:
        if dic["enabled"]:
            retrieved.append((dic["fullName"],dic["name"],int(dic["year"]),sum(dic["exercises"])))
    
    return retrieved

def retrieve_course(course_name: str)->dict:
    url=urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats")
    json_format=url.read()
    contents=json.loads(json_format)

    no_of_weeks=len(contents)
    no_of_students=-1
    hours=0
    exercises=0

    for key,values in contents.items():
        if values["students"]>no_of_students:
            no_of_students=values["students"]

        hours+=values["hour_total"]

        exercises+=values["exercise_total"]

    course={
        'weeks': no_of_weeks,
        'students': no_of_students,
        'hours': hours,
        'hours_average': math.floor(hours/no_of_students),
        'exercises': exercises,
        'exercises_average': math.floor(exercises/no_of_students)
        }

    return course

#who_cheated
import datetime
import csv

def cheaters()->list:
    start_time={}
    end_time={}
    cheater=[]

    with open("start_times.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            time=datetime.datetime.strptime(line[1],"%H:%M")
            start_time[line[0]]=time

    with open("submissions.csv") as file:
        for line in csv.reader(file, delimiter=";"):
            name = line[0]

            time=datetime.datetime.strptime(line[3],"%H:%M")
            
            if name not in end_time or time > end_time[name]:
                end_time[name] = time

    for student_id in start_time:
        if (end_time[student_id]-start_time[student_id]).total_seconds()>10800:
            cheater.append(student_id)

    return cheater

#who_cheated_2
import csv
from datetime import datetime, timedelta
 
def final_points():
    with open("start_times.csv") as start, open("submissions.csv") as submission:
        start_times = {}
        for row in csv.reader(start, delimiter=";"):
            name = row[0]
            time = datetime.strptime(row[1], "%H:%M")
            start_times[name] = time
 
        points = {}
        for row in csv.reader(submission, delimiter=";"):
            name = row[0]
            tno = int(row[1])
            p = int(row[2])
            time = datetime.strptime(row[3], "%H:%M")
 
            if time - start_times[name] > timedelta(hours=3):
                continue
 
            if name not in points:
                default_time = datetime(1900, 1, 1)
                points[name] = {}
                for i in range(1, 8+1):
                    points[name][i] = 0
                points[name][tno] = p
 
            elif p > points[name][tno]:
                points[name][tno] = p
 
        final_points = {}
        for student in points:
            p = 0
            for exercise in points[student]:
                p += points[student][exercise]
            final_points[student] = p
 
        return final_points

#spellchecker_2
import difflib

word=input("please type some text: ")

words=[]
with open("wordlist.txt") as file:
    for line in file:
        line=line.strip()
        words.append(line)

word=word.split()
misspelled=[]
for i,text in enumerate(word):
    if i==0:
        new=text.lower()
        if new not in words:
            word[i]=f"*{text}*"
    elif text not in words:
        word[i]=f"*{text}*"
        misspelled.append(text)

print(" ".join(word))
print("suggestions:")
for word in misspelled:
    match=difflib.get_close_matches(word,words)
    print(f"{word}: {", ".join(match)}")

#string_helper
import string

def change_case(orig_string: str)->str:
    return orig_string.swapcase()

def split_in_half(orig_string: str):
    half=len(orig_string)//2
    return (orig_string[:half],orig_string[half:])

def remove_special_characters(orig_string: str):
    modified_string=""
    for s in orig_string:
        if s in string.ascii_letters or s in string.digits or s in " ":
            modified_string+=s
    
    return modified_string
