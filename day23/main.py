from collections import defaultdict

def parse(lines):
    graph = defaultdict(set)
    for line in lines:
        a, b = line.split('-')
        graph[a].add(b)
        graph[b].add(a)
    return graph

def try_grow_clique(graph, clique):
    possible = set.intersection(*(graph[node] for node in clique)) - clique
    for other in possible:
        yield clique | {other}

def gen_cliques(graph, consider=None, min_size=-1, max_size=-1):
    cliques = {frozenset((node,)) for node in (consider or graph)}
    while cliques:
        new_cliques = set()
        while cliques:
            head = cliques.pop()
            if max_size != -1 and len(head) > max_size:
                return
            if len(head) >= min_size:
                yield head
            for new in try_grow_clique(graph, head):
                new_cliques.add(new)
        cliques = new_cliques

def solve_p1(lines):
    graph = parse(lines)
    t_nodes = [node for node in graph if node.startswith('t')]
    return sum(1 for clique in set(gen_cliques(graph, t_nodes, 3, 3)))

def solve_p2(lines):
    return ','.join(sorted(max(gen_cliques(parse(lines)), key=len)))
