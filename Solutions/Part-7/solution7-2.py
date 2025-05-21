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