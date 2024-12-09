def seq_sum(idx, length):
    return int(length * ((idx * 2 - 1) + length) / 2)

def parse(lines):
    files = []
    gaps = []
    offset = 0
    do_file = True
    for x in map(int, ''.join(lines)):
        if x > 0:
            (files if do_file else gaps).append([offset, x])
            offset += x
        do_file = not do_file
    return files, gaps

def solve_p1(lines):
    files, gaps = parse(lines)
    checksum = 0
    gap_iter = iter(gaps)
    gap = next(gap_iter)
    for file_idx in range(len(files) - 1, -1, -1):
        file = files[file_idx]
        while file[1] > 0 and file[0] + file[1] > gap[0]:
            moved = min(file[1], gap[1])
            checksum += file_idx * seq_sum(gap[0], moved)
            gap[0] += moved
            gap[1] -= moved
            file[1] -= moved
            if gap[1] == 0:
                gap = next(gap_iter)
        checksum += file_idx * seq_sum(file[0], file[1])
    return checksum

def solve_p2(lines):
    files, gaps = parse(lines)
    checksum = 0
    for file_idx in range(len(files) - 1, -1, -1):
        file = files[file_idx]
        for gap_idx, gap in enumerate(gaps):
            if file[0] + file[1] <= gap[0]:
                break
            if file[1] <= gap[1]:
                file[0] = gap[0]
                gap[0] += file[1]
                gap[1] -= file[1]
                if gap[1] == 0:
                    gaps.pop(gap_idx)
                break
        checksum += file_idx * seq_sum(file[0], file[1])
    return checksum
