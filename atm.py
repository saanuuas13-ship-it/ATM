import sys

def atm(amount, balance, pin):
    if pin == 1234 and amount > 0 and amount <= balance:
        return "Approved"
    else:
        return "Declined"

amount = int(sys.argv[1])
balance = int(sys.argv[2])
pin = int(sys.argv[3])

print(atm(amount, balance, pin))