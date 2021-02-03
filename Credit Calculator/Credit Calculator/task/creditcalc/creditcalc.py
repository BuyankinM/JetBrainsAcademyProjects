import math
import argparse


def print_overpayment(principal, monthly_payment, periods):
    print(f"Overpayment = {monthly_payment * periods - principal}")


def calc_count_months(principal, monthly_payment):
    n_months = math.log(monthly_payment / (monthly_payment - i * principal), 1 + i)
    n_months_int = math.ceil(n_months)
    years, months = divmod(n_months_int, 12)

    period_string_mas = []
    if years:
        period_string_mas.append(f"{years} year{'s' if years > 1 else ''}")
    if months:
        period_string_mas.append(f"{months} month{'s' if months > 1 else ''}")
    period_string = " and ".join(period_string_mas)

    print(f"You need {period_string} to repay this credit!")
    print_overpayment(principal, monthly_payment, n_months_int)


def calc_annuity_payment(principal, periods):
    annuity_payment = math.ceil(principal * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
    print(f"Your annuity payment = {annuity_payment}!")
    print_overpayment(principal, annuity_payment, periods)


def calc_credit_principal(monthly_payment, periods):
    principal = math.floor(monthly_payment / ((i * (1 + i) ** periods) / ((1 + i) ** periods - 1)))
    print(f"Your credit principal = {principal}!")
    print_overpayment(principal, monthly_payment, periods)


def calc_diff_payment(principal, periods):

    total_principal = 0
    for m in range(1, periods + 1):
        monthly_payment = math.ceil((principal / periods) + i * (principal - principal * (m - 1) / periods))
        total_principal += monthly_payment
        print(f"Month {m}: paid out {monthly_payment}")

    print()
    print(f"Overpayment = {total_principal - principal}")


parser = argparse.ArgumentParser()
parser.add_argument("--type", help="Type of payments")
parser.add_argument("--payment", type=int, help="Monthly payment")
parser.add_argument("--principal", type=int, help="Size of credit")
parser.add_argument("--periods", type=int, help="Number of moths")
parser.add_argument("--interest", type=float, help="Percents")

args = parser.parse_args()
params = {"type", "payment", "principal", "periods", "interest"}
num_empty = sum(1 for key, value in args.__dict__.items() if key in params and not value)
i = args.interest / (12 * 100) if args.interest else 0

if num_empty > 2 \
        or args.type not in {"annuity", "diff"} \
        or args.type == "diff" and args.payment \
        or not args.interest \
        or args.interest < 0 \
        or args.payment and args.payment < 0 \
        or args.principal and args.principal < 0 \
        or args.periods and args.periods < 0:

    print("Incorrect parameters")

elif args.type == "annuity":

    if args.payment:
        if args.principal:
            calc_count_months(args.principal, args.payment)
        elif args.periods:
            calc_credit_principal(args.payment, args.periods)
    else:
        calc_annuity_payment(args.principal, args.periods)

elif args.type == "diff":

    calc_diff_payment(args.principal, args.periods)
