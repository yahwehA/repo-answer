salary = 5000
spend = 6000
months = 10
increase = 0.03
s = 0
for j in range(months):
    s += spend
    spend *= 1 + increase
money_capital = s - (salary * months)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
