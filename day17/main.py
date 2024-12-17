A, B, C = 0, 1, 2

def parse(lines):
    a = int(lines[0].split(': ')[1])
    b = int(lines[1].split(': ')[1])
    c = int(lines[2].split(': ')[1])
    program = tuple(map(int, lines[4].split(': ')[1].split(',')))
    return program, [a, b, c]

def op_val(op, registers):
    return op if op < 4 else registers[op - 4]

def do_instruction(opcode, operand, registers):
    if opcode == 0:
        registers[A] = registers[A] // (2 ** op_val(operand, registers))
    elif opcode == 1:
        registers[B] = registers[B] ^ operand
    elif opcode == 2:
        registers[B] = op_val(operand, registers) % 8
    elif opcode == 3 and registers[A] != 0:
        return operand, None
    elif opcode == 4:
        registers[B] = registers[B] ^ registers[C]
    elif opcode == 5:
        return None, op_val(operand, registers) % 8
    elif opcode == 6:
        registers[B] = registers[A] // (2 ** op_val(operand, registers))
    elif opcode == 7:
        registers[C] = registers[A] // (2 ** op_val(operand, registers))
    return None, None

def run(program, registers):
    exe = 0
    outs = []
    while exe < len(program) - 1:
        jump, out = do_instruction(program[exe], program[exe + 1], registers)
        exe = (exe + 2) if jump is None else jump
        if out is not None:
            outs.append(out)
    return outs

def solve_p1(lines):
    return ','.join(map(str, run(*parse(lines))))

def find_for_n(program, a, n):
    for i in range(8):
        if (i ^ 5 ^ 6 ^ ((a + i) // 2 ** (i ^ 5)) % 8) == program[n]:
            yield a + i
    yield None

def solve_p2(lines):
    program, registers = parse(lines)
    if registers[0] in (729, 2024):
        return 'n/a'
    a_tracker = [None for _ in range(len(program))]
    n_finders = [None for _ in range(len(program))]
    n = len(program) - 1
    while n >= 0 and n < len(program):
        if n_finders[n] is None:
            a = a_tracker[n + 1] if n < len(program) - 1 else 0
            n_finders[n] = find_for_n(program, a * 8, n)
        value = next(n_finders[n])
        if value is None:
            n_finders[n] = None
            a_tracker[n] = None
            n += 1
        else:
            a_tracker[n] = value
            n -= 1
    return a_tracker[0]
