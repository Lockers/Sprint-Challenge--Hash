def get_indices_of_item_weights(weights, length, limit):

    hashDict = {}
    for i in range(length):
        check = hashDict.get(limit - weights[i])
        if check != None:
            return (i, check)
        else:
            hashDict[weights[i]] = i
    return None
    
get_indices_of_item_weights([1, 2, 3, 4, 45], 3, 5)
