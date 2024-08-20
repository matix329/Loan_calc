import math
import sys

args = sys.argv

type = None
principal = None
payment = None
periods = None
interest = None

for arg in args:
    if arg.startswith("--type="):
        type = arg.split("=")[1]
    elif arg.startswith("--principal="):
        principal = float(arg.split("=")[1])
    elif arg.startswith("--payment="):
        payment = float(arg.split("=")[1])
    elif arg.startswith("--periods="):
        periods = int(arg.split("=")[1])
    elif arg.startswith("--interest="):
        interest = float(arg.split("=")[1])

if type not in ["annuity", "diff"] or interest is None or interest <= 0:
    print("Incorrect parameters")
    exit()

if (principal is not None and principal < 0) or \
   (payment is not None and payment < 0) or \
   (periods is not None and periods < 0):
    print("Incorrect parameters")
    exit()

params_count = sum(x is not None for x in [principal, payment, periods])

if params_count != 2:
    print("Incorrect parameters")
    exit()

if type == "diff":
    if payment is not None:
        print("Incorrect parameters")
    else:
        i = (interest / 100) / 12
        total_payment = 0
        for m in range(1, periods + 1):
            d = (principal / periods) + i * (principal - (principal * (m - 1) / periods))
            total_payment += math.ceil(d)
            print(f"Month {m}: payment is {math.ceil(d)}")
        overpayment = int(total_payment - principal)
        print(f"\nOverpayment = {overpayment}")

elif type == "annuity":
    i = (interest / 100) / 12
    if principal and payment:
        n = math.log(payment / (payment - i * principal), 1 + i)
        n = math.ceil(n)
        years = n // 12
        months = n % 12
        total_payment = math.ceil(payment * n)
        overpayment = int(total_payment - principal)
        if years == 0:
            print(f"It will take {months} months to repay this loan!")
        elif months == 0:
            print(f"It will take {years} years to repay this loan!")
        else:
            print(f"It will take {years} years and {months} months to repay this loan!")
        print(f"Overpayment = {overpayment}")

    elif principal and periods:
        annuity_payment = principal * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1)
        total_payment = math.ceil(annuity_payment) * periods
        overpayment = int(total_payment - principal)
        print(f"Your annuity payment = {math.ceil(annuity_payment)}!")
        print(f"Overpayment = {overpayment}")

    elif payment and periods:
        principal = payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
        principal = math.floor(principal)
        total_payment = math.ceil(payment) * periods
        overpayment = int(total_payment - principal)
        print(f"Your loan principal = {int(principal)}!")
        print(f"Overpayment = {overpayment}")

else:
    print("Incorrect parameters")
