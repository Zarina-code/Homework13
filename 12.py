per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
float_percent = per_cent.values()

int_money = int(input("money = "))


def function(p):
    return int_money / 100 * p


deposit = list(map(function, float_percent))

print("deposit = ", deposit)

print("Максимальная сумма, которую вы можете заработать - ", max(deposit))