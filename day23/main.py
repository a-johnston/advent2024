from collections import defaultdict

def canonical(*args):
    return tuple(sorted(args))

def parse(lines):
    graph = defaultdict(set)
    for line in lines:
        a, b = line.split('-')
        graph[a].add(b)
        graph[b].add(a)
    return graph

def try_grow_clique(graph, clique):
    possible = set.intersection(*(graph[node] for node in clique)) - set(clique)
    for other in possible:
        yield canonical(other, *clique)

def gen_cliques(graph, consider=None, min_size=-1, max_size=-1):
    cliques = {(node,) for node in (consider or graph)}
    yield from cliques
    while True:
        new_cliques = set()
        while cliques:
            head = cliques.pop()
            if max_size != -1 and len(head) > max_size:
                return
            if len(head) >= min_size:
                yield head
            new_cliques |= set(try_grow_clique(graph, head))
        cliques = new_cliques
        if not cliques:
            return

def solve_p1(lines):
    graph = parse(lines)
    t_nodes = [node for node in graph if node.startswith('t')]
    return sum(1 for clique in set(gen_cliques(graph, t_nodes, 3, 3)))

def solve_p2(lines):
    return ','.join(max(gen_cliques(parse(lines)), key=len))
