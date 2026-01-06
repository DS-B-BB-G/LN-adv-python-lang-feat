# Python code​​​​​​‌‌‌​‌‌‌​​‌‌​​​‌​​‌​‌​‌​‌‌ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

def calc_order_price(order_contents):
    # set the initial variables for the totals
    total_price = 0.0

    # Your code to calculate the total price goes here
    for item in order_contents:
        match item:
            # Dry Clean: use literal strings to make sure we match accepted garments
            case "shirt" | "pants" | "jacket" | "dress" as garment, size, starch, sameday:
                total_price += 12.95
                if starch:
                    total_price += 2.00
                if sameday:
                    total_price += 10.00

            # For wash and fold, capture the desc and make sure it's a string
            case str() as desc, weight:
                if weight >= 15.0:
                    total_price += (weight * 4.95) * .9
                else:
                    total_price += (weight * 4.95)

            # Blankets: again, use literal strings to ensure correct type
            case "comforter" | "cover" as blanket, dry_clean, size:
                total_price += 25.00
                if (dry_clean == True):
                    total_price += 5.00

            # unspecified / rest
            case _:
                print("invalid item format")

    # then return the result rounded to 2 places
    return round(total_price,2)


# This is how your code will be called.
# You can edit this code to try different testing cases.
test_order = [
    ["shirt", "L", True, False],
    ["pants", "M", False, True],
    ["dress", "M", False, True],
    ["cover", True, "L"],
    ["whites", 5.25],
    ["darks", 12.5],
    ["pants", "S", False, False],
    ["jacket", "L", False, True],
    ["shirts and jeans", 28.0],
    ["comforter", False, "L"],
    ["shirt", "L", True, True]
]

result = calc_order_price(test_order)

print(result)