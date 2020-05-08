def has_negatives(a):

    hashDict = {}
    items = []

    for x in a:
        # Check if absolute value of x is in hashDict
        # If number has a negative, add to items, else dont add to list (None)
        
        if abs(x) in hashDict:
            items += [abs(x)]
        else:
            hashDict[abs(x)] = None
    print(items)        
    return items


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
