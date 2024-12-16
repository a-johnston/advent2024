from adventlib import grid, util, vector

dirs = {'>': grid.east, '<': grid.west, 'v': grid.south, '^': grid.north}
reps = (('#', '##'), ('.', '..'), ('O', '[]'), ('@', '@.'))

def parse(lines, wide):
    rows, moves = util.split(lines)
    if wide:
        rows = [util.chain_replace(row, *reps) for row in rows]
    robot = next(grid.indexes(rows, '@'))
    walls = set(grid.indexes(rows, '#'))
    blocks = {}
    for block in ('O', '[', ']'):
        blocks.update({xy: block for xy in grid.indexes(rows, block)})
    return robot, blocks, walls, ''.join(moves)

def get_block_moves(pos, blocks, walls, d):
    if pos in walls:
        return None
    if pos not in blocks:
        return dict()
    moves = {pos: vector.add(pos, d)}
    if blocks[pos] == '[':
        right = vector.add(pos, grid.east)
        moves[right] = vector.add(right, d)
    elif blocks[pos] == ']' and d != grid.west:
        left = vector.add(pos, grid.west)
        moves[left] = vector.add(left, d)
    for subpos in tuple(moves.values()):
        if moves is not None and subpos not in moves:
            submoves = get_block_moves(subpos, blocks, walls, d)
            if submoves is None:
                return None
            moves.update(submoves)
    return moves

def do_move(robot, blocks, walls, d):
    new_pos = vector.add(robot, d)
    moves = get_block_moves(new_pos, blocks, walls, d)
    if moves is None:
        return robot
    for start, end in sorted(moves.items(), key=lambda move: -vector.dot(move[1], d)):
        blocks[end] = blocks[start]
        blocks.pop(start)
    return new_pos

def helper(robot, blocks, walls, moves):
    for move in moves:
        robot = do_move(robot, blocks, walls, dirs[move])
    return sum(j * 100 + i for i, j in blocks if blocks[(i, j)] != ']')

solve_p1 = lambda lines: helper(*parse(lines, False))
solve_p2 = lambda lines: helper(*parse(lines, True))
