def sum_distance(from_, to):
    """
    Суммирует все числа от from до to включительно.
    Если from > to, меняет их местами.
    """

    if from_ > to:
        from_, to = to, from_


    total = 0
    for i in range(from_, to + 1):
        total += i

    return total



print(sum_distance(3, 7))
print(sum_distance(10, 5))
print(sum_distance(1, 1))
print(sum_distance(-2, 1))
