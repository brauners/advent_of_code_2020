
class Instruction():
    def __init__(self, operation, argument):
        self.operation = operation
        self.argument = int(argument)
        self.is_visited = False


def interpret_instruction(instruction):
    acc_change = 0
    offset = 0
    if instruction.operation == "acc":
        acc_change = instruction.argument
        offset = 1
    elif instruction.operation == "jmp":
        offset = instruction.argument
    elif instruction.operation == "nop":
        offset = 1
    instruction.is_visited = True
    return acc_change, offset

if __name__ == "__main__":
    input_filename = "day_08/input"
    # input_filename = "day_08/input_debug"
    with open(input_filename) as fp:
        instructions = [Instruction(*line.split()) for line in fp.readlines()]

    accumulator = 0
    current_instruction_idx = 0
    while True:
        instruction = instructions[current_instruction_idx]
        if instruction.is_visited:
            print("Has been visited.")
            break
        accumulator_change, idx_offset = interpret_instruction(instruction)
        accumulator += accumulator_change
        current_instruction_idx += idx_offset
        current_instruction_idx = current_instruction_idx % len(instructions)
    
    print(f"Accumulatos: {accumulator}")