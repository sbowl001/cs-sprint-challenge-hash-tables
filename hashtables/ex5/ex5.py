# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}
    found_files = []
    for file in files: 
        parts = file.split("/")
        key = parts[-1]

        if key not in cache: 
            cache[key] = []

        cache[key].append(file)

    for query in queries: 
        if query in cache: 
            found_files += cache[query]
    return found_files


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
