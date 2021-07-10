def LineAnalysis(line):
    if '.' not in line:
        return True
    mid = len(line) // 2
    if len(line) % 2 == 0:
        if line[:mid] == line[-1:-mid - 1:-1]:
            return True
        else:
            return False
    else:
        if line[:mid + 1] == line[-1:-mid - 2:-1]:
            return True
        else:
            return False
