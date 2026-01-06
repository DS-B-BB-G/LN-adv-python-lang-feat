def string_combiner(*args, unique=False):
    """
    string_combiner(*args, unique=False)
    Returns a string that merges all strings and ints in 'args'.
    Parameters:
    args: one or more strings and int. Other types are ignored.
    unique: if True, the result string contains only 1 instance 
    of each character
    """
    combined = ""
    for arg in args:
        if isinstance(arg, int):
            combined += str(arg)
        elif isinstance(arg, str):
            combined += arg

    # if unique is true, we need to convert to a set and then a string
    if unique:
        newresult = set(combined)
        combined = "".join(newresult)

    return combined


# items = ["This", "is", 1, True, "string!"]
# also try different values for useUnique
items = ["This", "is", 0.1, "test", "string!"]
# items = ["This", "is", [1, 2], "string!"]
useUnique = False  # False or True

result = string_combiner(*items, unique=useUnique)

print(result)
