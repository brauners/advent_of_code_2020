
class Instruction():
    def __init__(self, operation, argument, is_visited=False):
        self.operation = operation
        self.argument = int(argument)
        self.is_visited = is_visited

def toggle_jmp_nop(instruction):
    ret = Instruction(instruction.operation, instruction.argument, instruction.is_visited)
    if ret.operation == "jmp":
        ret.operation = "nop"
    else:
        ret.operation = "jmp"
    return ret

def interpret_instruction(instruction, set_visited=True):
    acc_change = 0
    offset = 0
    if instruction.operation == "acc":
        acc_change = instruction.argument
        offset = 1
    elif instruction.operation == "jmp":
        offset = instruction.argument
    elif instruction.operation == "nop":
        offset = 1
    instruction.is_visited = set_visited
    return acc_change, offset

if __name__ == "__main__":
    input_filename = "day_08/input"
    # input_filename = "day_08/input_debug"
    with open(input_filename) as fp:
        instructions = [Instruction(*line.split()) for line in fp.readlines()]

    current_instruction_idx = len(instructions) - 1
    has_previous = True
    # Find the lost link
    while has_previous:
        for idx, instruction in enumerate(instructions):
            _, offset = interpret_instruction(instruction, set_visited=False)
            if idx + offset == current_instruction_idx:
                # previous instruction was found
                current_instruction_idx = idx
                has_previous = True
                break
            else:
                has_previous = False

    lost_link_idx = current_instruction_idx

    for idx, instruction in enumerate(instructions):
        if instruction.operation in ["nop", "jmp"]:
            instruction = toggle_jmp_nop(instruction)
            _, offset = interpret_instruction(instruction, set_visited=False)
            if idx + offset == lost_link_idx:
                instructions[idx] = instruction
                break


    accumulator = 0
    current_instruction_idx = 0
    while True:
        instruction = instructions[current_instruction_idx]
        if instruction.is_visited:
            print("Has been visited.")
            break
        accumulator_change, idx_offset = interpret_instruction(instruction)
        accumulator += accumulator_change
        if current_instruction_idx == len(instructions) - 1:
            break
        current_instruction_idx += idx_offset
        current_instruction_idx = current_instruction_idx % len(instructions)
    
    print(f"Accumulatos: {accumulator}")