def get_indices_of_item_weights(weights, length, limit):

    hashDict = {}
    for i in range(length):
        check = hashDict[limit - weights[i]]
        if check != None:
            return (i, check)
        else:
            hashDict[weights[i]] = i
    return None
    
get_indices_of_item_weights(1, 3, 5)
