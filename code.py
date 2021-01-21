def are_valid_groups2(a, b):
    x = set(a)
    if (len(x)!= len(a)):
        return False

    for i in range(len(b)):
        if (len(b[i]) != 2) and (len(b[i]) != 3):
            return False

    return True

	
