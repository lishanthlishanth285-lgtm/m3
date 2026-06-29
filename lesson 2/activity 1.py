def cal(bill,tip):
    tip = (bill * tip) / 100
    amt = bill + tip
    print(f"the tip amount is: {tip} \n the bill amount is: {bill} \n the total amount is: {amt}")

cal(300,10)