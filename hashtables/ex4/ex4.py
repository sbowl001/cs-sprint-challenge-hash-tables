def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {} 

    # positive_numbers = list(filter(lambda x: x > 0, a))

    # for x in a: 
    #     if -x in positive_numbers:
    #         cache[-x] = True 
    

    # return list(cache)

    # try 2 
    positive_numbers = [] 

    for x in a: 
        cache[x] = 1 
        if x != 0 and x * -1 in cache: 
            positive_numbers.append(abs(x))
    return positive_numbers 


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
