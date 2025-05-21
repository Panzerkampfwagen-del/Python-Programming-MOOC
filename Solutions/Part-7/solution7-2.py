'''
PRINT [value]: prints the value
MOV [variable] [value]: assigns the value to the variable
ADD [variable] [value]: adds the value to the variable
SUB [variable] [value]: subtracts the value from the variable
MUL [variable] [value]: multiplies the variable by the value
[location]:: names a line of code, so it can be jumped to from elsewhere
JUMP [location]: jumps to the location specified
IF [condition] JUMP [location]: if the condition is true, jump to the location specified
END: finish execution

The square brackets above are just a notation to signify operands; see below for usage examples.

The program is executed line by line from the first line onwards. The execution ends when the executor comes across the command END, or when there are no more lines to execute.

Each program has 26 pre-defined variables, named A to Z. Each variable has the value 0 when the program begins. The notation [variable] refers to one of these 26 variables.

All the values processed by the program are integer numbers. The notation [value] refers either to a value stored in a variable, or an integer number typed in directly.

The notation [location] refers to any name of a location which consists of lowercase letters a to z and/or numbers 0 to 9. Two different locations may not have the same name.

The notation [condition] refers to any expression in the format [value] [comparison] [value], where [comparison] is one of the following operators: ==, !=, <, <=, > and >=
'''

#own_language
def run(instructions: list) -> list:
    stack = [0] * 26
    pre_variables = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    track = {}

    for idx, line in enumerate(instructions):
        if ":" in line:
            parts = line.split(":")
            label = parts[0]
            track[label] = idx
            instructions[idx] = ""

    i = 0
    while i < len(instructions):
        line = instructions[i]
        if line == "END":
            break
        if not line:
            i += 1
            continue

        instruction = line.split()
        op = instruction[0]

        def get_value(val):
            return stack[pre_variables.index(val)] if val in pre_variables else int(val)

        if op == "MOV":
            pos = pre_variables.index(instruction[1])
            stack[pos] = get_value(instruction[2])

        elif op == "ADD":
            p1 = pre_variables.index(instruction[1])
            stack[p1] += get_value(instruction[2])

        elif op == "SUB":
            p1 = pre_variables.index(instruction[1])
            stack[p1] -= get_value(instruction[2])

        elif op == "MUL":
            p1 = pre_variables.index(instruction[1])
            stack[p1] *= get_value(instruction[2])

        elif op == "JUMP":
            label = instruction[1]
            i = track[label]
            continue

        elif op == "IF":
            jump_index = instruction.index("JUMP")
            condition = " ".join(instruction[1:jump_index])
            label = instruction[jump_index + 1]
            env = {ch: stack[pre_variables.index(ch)] for ch in pre_variables}
            if eval(condition, env):
                i = track[label]
                continue

        elif op == "PRINT":
            val = instruction[1]
            result.append(get_value(val))

        i += 1

    return result

#Examples
#1
program1 = []
program1.append("MOV A 1")
program1.append("MOV B 2")
program1.append("PRINT A")
program1.append("PRINT B")
program1.append("ADD A B")
program1.append("PRINT A")
program1.append("END")
result = run(program1)
print(result)

#Sample output
[1, 2, 3]

#2
program2 = []
program2.append("MOV A 1")
program2.append("MOV B 10")
program2.append("begin:")
program2.append("IF A >= B JUMP quit")
program2.append("PRINT A")
program2.append("PRINT B")
program2.append("ADD A 1")
program2.append("SUB B 1")
program2.append("JUMP begin")
program2.append("quit:")
program2.append("END")
result = run(program2)
print(result)

#Sample output
[1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

#3
program3 = []
program3.append("MOV A 1")
program3.append("MOV B 1")
program3.append("begin:")
program3.append("PRINT A")
program3.append("ADD B 1")
program3.append("MUL A B")
program3.append("IF B <= 10 JUMP begin")
program3.append("END")
result = run(program3)
print(result)

#Sample output
[1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]

#4
program4 = []
program4.append("MOV N 50")
program4.append("PRINT 2")
program4.append("MOV A 3")
program4.append("begin:")
program4.append("MOV B 2")
program4.append("MOV Z 0")
program4.append("test:")
program4.append("MOV C B")
program4.append("new:")
program4.append("IF C == A JUMP error")
program4.append("IF C > A JUMP over")
program4.append("ADD C B")
program4.append("JUMP new")
program4.append("error:")
program4.append("MOV Z 1")
program4.append("JUMP over2")
program4.append("over:")
program4.append("ADD B 1")
program4.append("IF B < A JUMP test")
program4.append("over2:")
program4.append("IF Z == 1 JUMP over3")
program4.append("PRINT A")
program4.append("over3:")
program4.append("ADD A 1")
program4.append("IF A <= N JUMP begin")
result = run(program4)
print(result)

#Sample output
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]