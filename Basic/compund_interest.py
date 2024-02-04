def ci(principal, rate, time):
    amount = principal * (1 + rate/100) ** time
    return amount - principal

principal = int(input())
rate = float(input())
time = int(input())

print(ci(principal, rate, time))