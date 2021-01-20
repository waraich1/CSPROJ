def are_valid_groups2(a, b):
    x = set(a)
    if (len(x) != len(a)):
        return False

    for i in b:
        if (len(i) != 2) and (len(i) != 3):
            return False

    return True

	
