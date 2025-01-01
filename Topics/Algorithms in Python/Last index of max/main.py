def last_indexof_max(numbers):
    # write the modified algorithm here
    idxmax = 0
    for i in range(len(numbers)):
        if numbers[i] >= numbers[idxmax]:
            idxmax = i
    return idxmax