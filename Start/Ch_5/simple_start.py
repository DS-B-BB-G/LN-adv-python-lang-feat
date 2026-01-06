# Example file for Advanced Python: Language Features by Joe Marini
# Simple pattern matching using literal values

x = "zero"

# TODO: Literal patterns are explicit values: integers, strings, Booleans, etc
match x:
    case 0:
        print("zero")
    case 1:
        print("one")
    case "zero":
        print(0)
    case None:
        print("Nothing")
    case _:
        print("others")
