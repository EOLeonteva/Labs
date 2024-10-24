money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

month_quantity = 0
while money_capital + salary - spend >= 0:
    if month_quantity != 0:
        spend = spend + (spend * increase)
    money_capital = money_capital + salary - spend
    month_quantity += 1
print("Количество месяцев, которое можно протянуть без долгов:",month_quantity)
