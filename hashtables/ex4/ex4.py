def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {} 

    positive_numbers = list(filter(lambda x: x > 0, a))

    for x in a: 
        if -x in positive_numbers:
            cache[-x] = True 
    

    return list(cache)


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
