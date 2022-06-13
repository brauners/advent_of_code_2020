from copy import deepcopy
class Instruction():
    def __init__(self, operation, argument, is_visited=False):
        self.operation = operation
        self.argument = int(argument)
        self.is_visited = is_visited

def toggle_jmp_nop(instruction):
    if instruction.operation == "jmp":
        instruction.operation = "nop"
    else:
        instruction.operation = "jmp"

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

def run_instructions(instructions):
    """Execute the instructions

    Returns:
        The accumulator value after executing the instructions.
        Return None if the execution runs in a infinite loop.
    """
    accumulator = 0
    current_instruction_idx = 0
    while True:
        instruction = instructions[current_instruction_idx]
        if instruction.is_visited:
            return None
        accumulator_change, idx_offset = interpret_instruction(instruction)
        accumulator += accumulator_change
        if current_instruction_idx == len(instructions) - 1:
            return accumulator
        current_instruction_idx += idx_offset
        current_instruction_idx = current_instruction_idx % len(instructions)


def swap_next_jmp_nop(instructions, after_idx):
    ret_instructions = deepcopy(instructions)
    for i in range(after_idx, len(instructions)):
        instruction = ret_instructions[i]
        if instruction.operation in ["jmp", "nop"]:
            toggle_jmp_nop(instruction)
            return i, ret_instructions


if __name__ == "__main__":
    input_filename = "day_08/input"
    # input_filename = "day_08/input_debug"
    with open(input_filename) as fp:
        instructions = [Instruction(*line.split()) for line in fp.readlines()]

    swap_from = 0 # Only swap jmp and nop after this index
    new_instructions = deepcopy(instructions)
    while True:
        accumulator = run_instructions(new_instructions)
        if accumulator is not None:
            # Execution ran til the end and is considered done
            break
        # Try swapping next jmp or nop
        last_swapped, new_instructions = swap_next_jmp_nop(instructions, swap_from)
        swap_from = last_swapped + 1
        
    
    
    print(f"Accumulator: {accumulator}")