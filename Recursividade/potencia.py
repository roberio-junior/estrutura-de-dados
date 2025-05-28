def pot (n: int, p: int) -> int:
    if p == 1:
        return n
    return n * pot(n, p-1)