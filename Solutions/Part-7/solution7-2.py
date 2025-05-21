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
    pre_variables = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result=[]
    track={}
    stack=[0]*26

    for i,instruction in enumerate(instructions):
        if ":" in instruction:
            pos=instruction.split(":")
            label=pos[0]
            track[label]=i
            instructions[i]=""

    i=0
    while i<len(instructions):
        if instructions[i]=="END":
            return result
        
        if instructions[i]=="":
            i+=1
            continue
        
        instruction=instructions[i].split()
        ops=instruction[0]
        
        if ops=="ADD":
            pos=pre_variables.index(instruction[1])
            if instruction[2] in pre_variables:
                val=pre_variables.index(instruction[2])
                stack[pos]+=stack[val]
            else:
                val=int(instruction[2])
                stack[pos]+=val

        elif ops=="SUB":
            pos=pre_variables.index(instruction[1])
            if instruction[2] in pre_variables:
                val=pre_variables.index(instruction[2])
                stack[pos]-=stack[val]
            else:
                val=int(instruction[2])
                stack[pos]-=val
            

        elif ops=="MUL":
            pos=pre_variables.index(instruction[1])
            if instruction[2] in pre_variables:
                val=pre_variables.index(instruction[2])
                stack[pos]*=stack[val]
            else:
                val=int(instruction[2])
                stack[pos]*=val

        elif ops=="MOV":
            pos=pre_variables.index(instruction[1])
            if instruction[2] in pre_variables:
                val=pre_variables.index(instruction[2])
                stack[pos]=stack[val]
            else:
                val=int(instruction[2])
                stack[pos]=val


        elif ops=="PRINT":
            if instruction[1] in pre_variables:
                val=pre_variables.index(instruction[1])
                result.append(stack[val])
            else:
                val=int(instruction[1])
                result.append(val)

        elif ops=="JUMP":
            label=instruction[1]
            i=track[label]
            continue

        elif ops=="IF":
            condition="".join([instruction[1],instruction[2],instruction[3]])
            env={ch:stack[pre_variables.index(ch)] for ch in pre_variables}
            if eval(condition,{},env):
                label=instruction[5]
                i=track[label]
                continue
        i+=1

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