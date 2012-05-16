def greatest(list):
    if len(list) == 0:
        return 0
    bsf = 0
    for item in list:
        if item > bsf:
            bsf = item
    return bsf