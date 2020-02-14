
def h_index(citations):
    citations.sort(reverse=True)
    for i, v in enumerate(citations):
        if v <= i:
            return i
    return 0

