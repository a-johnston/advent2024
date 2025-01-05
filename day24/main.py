from collections import defaultdict, namedtuple
import operator

Gate = namedtuple('Gate', ('op', 'a', 'b', 'out'))

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
                if gate.a in state and gate.b in state:
                    seen.add(gate.out)
                    new_assigned.add(gate.out)
                    op = operator_lookup[gate.op]
                    state[gate.out] = op(state[gate.a], state[gate.b])
        assigned = new_assigned
    total = 0
    for k in sorted((k for k in state if k[0] == 'z'), reverse=True):
        total = total * 2 + state[k]
    return total

def parse(lines):
    state, gates = (x.split('\n') for x in '\n'.join(lines).split('\n\n'))
    state = {k: int(v) for k, v in (s.split(': ') for s in state)}
    vars_to_gates = defaultdict(list)
    for line in gates:
        lh, out = line.split(' -> ')
        a, op, b = lh.split()
        gate = Gate(op, a, b, out)
        vars_to_gates[a].append(gate)
        vars_to_gates[b].append(gate)
    return state, vars_to_gates

def solve_p1(lines):
    return simulate(*parse(lines))

def solve_p2(lines):
    state, vars_to_gates = parse(lines)
    otg = {gate.out: gate for gate in set.union(*map(set, vars_to_gates.values()))}
    if len(state) < 90:
        return 'n/a'
    wrong = set()
    for gate in otg.values():
        if gate.op == 'XOR':
            if gate.a not in otg or gate.b not in otg:
                if gate.out[0] == 'z' and gate.out != 'z00':
                    wrong.add(gate.out)
            elif gate.out[0] != 'z':
                wrong.add(gate.out)
        if gate.out[0] == 'z':
            if gate.op != 'XOR' and gate.out != 'z45':
                wrong.add(gate.out)
        else:
            if gate.op == 'OR':
                for arg in (gate.a, gate.b):
                    if arg not in otg or otg[arg].op != 'AND':
                        wrong.add(arg)
            if gate.op == 'AND':
                for arg in (gate.a, gate.b):
                    if arg in otg and otg[arg].op == 'AND':
                        if 'x00' not in (otg[arg].a, otg[arg].b):
                            wrong.add(arg)
    return ','.join(sorted(wrong))
