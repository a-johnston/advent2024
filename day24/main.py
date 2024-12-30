from collections import defaultdict, namedtuple
import operator

Gate = namedtuple('Gate', ('op', 'args', 'out'))

operator_lookup = { 'XOR': operator.xor, 'AND': operator.and_, 'OR': operator.or_ }

def simulate(state, vars_to_gates):
    assigned = {k for k in state if k[0] in {'x', 'y'}}
    seen = set()
    while assigned:
        new_assigned = set()
        for node in assigned:
            for gate in vars_to_gates[node]:
                if gate.out in seen:
                    continue
                if all(arg in state for arg in gate.args):
                    seen.add(gate.out)
                    new_assigned.add(gate.out)
                    args = (state[arg] for arg in gate.args)
                    state[gate.out] = operator_lookup[gate.op](*args)
        assigned = new_assigned
    total = 0
    for k in sorted((k for k in state if k[0] == 'z'), reverse=True):
        total = total * 2 + state[k]
    return total

def parse(lines):
    it = iter(lines)
    vars_in = {}
    vars_to_gates = defaultdict(list)
    outs_to_gate = {}
    for line in it:
        if not line:
            break
        idx, val = line.split(': ')
        vars_in[idx] = int(val)
    for line in it:
        lh, out = line.split(' -> ')
        a, op, b = lh.split()
        args = {a, b}
        gate = Gate(op, args, out)
        for arg in args:
            vars_to_gates[arg].append(gate)
        outs_to_gate[out] = gate
    return vars_in, vars_to_gates, outs_to_gate

def solve_p1(lines):
    return simulate(*parse(lines)[:2])

def solve_p2(lines):
    _, __, otg = parse(lines)
    if len(gates.state) < 90:
        return 'n/a'
    otg = gates.outs_to_gate
    wrong = set()
    for gate in otg.values():
        if gate.op == 'XOR':
            if any(x[0] in {'x', 'y'} for x in gate.args):
                if gate.out[0] == 'z' and gate.out != 'z00':
                    wrong.add(gate.out)
            elif gate.out[0] != 'z':
                wrong.add(gate.out)
        if gate.out[0] == 'z':
            if gate.op != 'XOR' and gate.out != 'z45':
                wrong.add(gate.out)
        else:
            if gate.op == 'OR':
                for arg in gate.args:
                    if arg not in otg or otg[arg].op != 'AND':
                        wrong.add(arg)
            if gate.op == 'AND':
                for arg in gate.args:
                    if arg in otg and otg[arg].op == 'AND':
                        if 'x00' not in otg[arg].args:
                            wrong.add(arg)
    return ','.join(sorted(wrong))
