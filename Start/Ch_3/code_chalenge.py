# Python code​​​​​​‌‌‌​‌‌‌​​‌​‌‌​​‌​​‌‌​‌‌​‌ below
# Use print("messages...") to debug your solution.
import string

show_expected_result = False
show_hints = False

l = 0
num_chars = 0
num_punct = 0
num_unique = 0
unique_str = ""

def calc_values(the_str):
    global l, num_chars, num_punct, num_unique, unique_str

    # YOUR CODE GOES HERE
    # Just set the values of the global variables,
    # there is no need to return a value from this function

    # length of given string (65)
    l = len(the_str)
    print(l)

    # count number of numeric characters (7)
    num_chars = len([c for c in the_str if c.isnumeric()])
    print(num_chars)

    # count number of punctuation characters (10)
    num_punct = len([c for c in the_str if c in string.punctuation])
    print(num_punct)

    # count number of unique characters (14)
    unique_str = "".join({c for c in the_str if c.isalpha()})
    num_unique = len(unique_str)
    print(num_unique)

    # return unique alphabetic string (lrMiokaJwgsenp)
    print(unique_str)


# This is how your code will be called. Feel free to edit the test string
# and try out some different test cases.
test_str = "2 apples, 9 oranges?, 4 pears, Mike's 1 egg, Jane's 2 kiwis, $50!"
calc_values(test_str)