item = input("Enter the item name: ")
item_price = float(input("Enter the price of the item: "))
given_amount = float(input("Enter the given amount: "))

if given_amount > item_price:
    print("The change amount is:", given_amount - item_price)
elif given_amount < item_price:
    print("You have to pay:", item_price - given_amount, "more to complete the payment.")
elif given_amount == item_price:
    print("You have given the exact amount.")