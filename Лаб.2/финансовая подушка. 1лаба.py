money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05
month = 1
while spend < money_capital:
    if month == 1:
        month += 1
        money_capital += salary - spend
    else:
        month += 1
        spend *= 1 + increase
        money_capital += salary - spend
print("Количество месяцев, которое можно протянуть без долгов:", month)





