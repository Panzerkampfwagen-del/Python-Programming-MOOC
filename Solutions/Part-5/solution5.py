#go
def who_won(game_board: list) -> int:
    player1=0
    player2=0
    for i in range(len(game_board)):
        for j in range(len(game_board[i])):
            if game_board[i][j] == 1:
                player1 += 1
            elif game_board[i][j] == 2:
                player2 += 1

    if player1>player2:
        return 1
    elif player2>player1:
        return 2
    else:
        return 0
            
    
if __name__ == "__main__":
    print(who_won([[1, 2, 1], [2, 1, 2], [1, 2, 1]]))

#sudoku_row
def row_correct(sudoku: list, row_no: int) -> bool:
        for j in range(len(sudoku[row_no])):
                new_list=[num for num in sudoku[row_no] if num != 0]
                new_set = set(new_list)
                return len(new_set) == len(new_list)
        
#sudoku_column
def column_correct(sudoku: list, column_no: int) -> bool:
    new_list=[]
    for i in range(len(sudoku)):
        new_list.append(sudoku[i][column_no])
        new_List=[num for num in new_list if num != 0]
        new_set=set(new_List)
    return len(new_set)==len(new_List)

#sudoku_block
def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    List=[]
    for i in range(row_no,row_no+3):
        for j in range(column_no,column_no+3):
            List.append(sudoku[i][j])
            List=[num for num in List if num !=0 ]
            Set=set(List)
    return len(Set)==len(List)

#sudoku_grid
def row_correct(sudoku: list, row_no: int) -> bool:
    row = sudoku[row_no]
    filtered_row = [num for num in row if num != 0]
    return len(filtered_row) == len(set(filtered_row))  

def column_correct(sudoku: list, column_no: int) -> bool:
    column = [row[column_no] for row in sudoku]
    filtered_column = [num for num in column if num != 0]
    return len(filtered_column) == len(set(filtered_column))

def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    block = []
    for i in range(3):  
        for j in range(3):
            if row_no + i < len(sudoku) and column_no + j < len(sudoku[0]):
                block.append(sudoku[row_no + i][column_no + j])
    
    filtered_block = [num for num in block if num != 0]
    return len(filtered_block) == len(set(filtered_block)) 

def sudoku_grid_correct(sudoku: list) -> bool:
    for row_no in range(9):
        if not row_correct(sudoku, row_no):
            return False
    
    for column_no in range(9):
        if not column_correct(sudoku, column_no):
            return False
    
    block_indices = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
    for row_no, column_no in block_indices:
        if not block_correct(sudoku, row_no, column_no):
            return False
    
    return True

#sudoku_print_and_add
def print_sudoku(sudoku: list) -> None:
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                if(j+1)%3==0:
                    if j==8:
                        print("_")
                    else:
                        print("_  ",end="")
                else:
                    print("_ ",end="")
            else:
                if(j+1)%3==0:
                    if j==8:
                        print(sudoku[i][j])
                    else:
                        print(f"{sudoku[i][j]}  ",end="")
                else:
                    print(f"{sudoku[i][j]} ",end="")

        if (1+i)%3 == 0:
            if i==8:
                break
            else:
                print() 

def add_number(sudoku: list, row_no: int, column_no: int, number: int) -> None:
    if 1 <= number <= 9 and 0 <= row_no < 9 and 0 <= column_no < 9:
        sudoku[row_no][column_no] = number

#sudoku_add_to_copy
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int) -> list:
    sudoku_copy = [row[:] for row in sudoku]
    
    if 1 <= number <= 9 and 0 <= row_no < 9 and 0 <= column_no < 9:
        sudoku_copy[row_no][column_no] = number

    return sudoku_copy

def print_sudoku(sudoku: list) -> None:
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                print("_", end=" ")
            else:
                print(sudoku[i][j], end=" ")

            if (j + 1) % 3 == 0 and j < 8:
                print(" ", end="")
        print()
        if (i + 1) % 3 == 0 and i < 8:
            print()

#tic_tac_toe
def play_turn(game_board: list, x: int, y: int, piece: str) -> bool:
    if not (0 <= x < 3 and 0 <= y < 3):
        return False
    if piece not in ("X", "O"):
        return False
    
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    else:
        return False
    
#phone_book_v1
def phone_book():
    phone_book_dict = {}

    while True:
        command = input("command (1 search, 2 add, 3 quit): ")

        if command == "1": 
            name = input("name: ")
            if name in phone_book_dict:
                print(phone_book_dict[name])
            else:
                print("no number")

        elif command == "2": 
            name = input("name: ")
            number = input("number: ")
            phone_book_dict[name] = number
            print("ok!")

        elif command == "3": 
            print("quitting...")
            break

        else:
            print("Invalid command")

phone_book()

#phone_book_v2
def phone_book():
    book = {}
    while True:
        command = int(input("command (1 search, 2 add, 3 quit):"))

        if command==1:
            name = input("name: ")
            if name in book:
                for number in book[name]:
                    print(number)
            else:
                print("no number")

        elif command==2:
            name=input("name: ")
            number=input("number: ")
            if name in book:
                book[name].append(number)
                print("ok!")
            else:
                book[name]=[number]
                print("ok!")

        elif command==3:
            print("quitting...")
            break

phone_book()

#numbers_spelled_out
def dict_of_numbers():
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["","","twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    # Create the dictionary
    number_dict = {}
    for i in range(10):
        number_dict[i]=ones[i]

    for i in range(10,20):
        number_dict[i]=teens[i-10]

    for i in range(20,100):
        List = list(str(i))
        if i % 10 == 0:
            number_dict[i]=tens[int(List[0])]
        else:
            number_dict[i]=tens[int(List[0])]+"-"+ones[int(List[1])]

    return number_dict

#student_database
def add_student(students: dict, name: str):
    students[name]=[]

def add_course(students: dict, name: str, course: tuple):
    cname, grade = course
    if grade==0:
        return
        
    for i,(existing_name,existing_grade) in enumerate(students[name]):
        if cname == existing_name:
            if grade > existing_grade:
                students[name][i]=(existing_name,grade)
            return

    students[name].append(course)

def print_student(students: dict, name: str):
    if name in students and students[name]==[]:
        print(name+":\n no completed courses")

    elif name not in students:
        print(f"{name}: no such person in the database")

    elif name in students:
        print(f"{name}:\n {len(students[name])} completed courses:")
        sum=0
        for course, grade in students[name]:
            print(f"  {course} {grade}")
            sum+=grade
        print(f" average grade {sum/len(students[name])}")

def summary(students: dict):
    print(f"students {len(students)}")
    
    most=0
    Name=None
    for name,courses in students.items():
        Len= len(courses)   
        if Len>most:
            most=Len
            Name=name

    best_avg=0
    bestName=None
    for name,courses in students.items():
        sum=0
        for cname,grade in courses:
            sum+=grade
        avg=sum/len(courses)
        if avg>best_avg:
            best_avg=avg
            bestName=name

    print(f"most courses completed {most} {Name}")
    print(f"best average grade {best_avg} {bestName}")

#letter_square
layers=int(input("layers:"))

for i in range(2*layers-1):
    for j in range(2*layers-1):
        left=j
        right=(2*layers-2)-j
        top=i
        bottom=(2*layers-2)-i
        alpha = min(left,right,top,bottom)
        print(chr(layers-alpha+64),end="")
    print()

