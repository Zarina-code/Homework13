tickets_amount = int(input("amount of the tickets: \n"))
sum_to_pay = 0
for i in range(tickets_amount):
    age = int(input("age: \n"))
    if 18 <= age < 25:
        sum_to_pay += 990
    elif age >= 25:
        sum_to_pay += 1390
if tickets_amount > 3:
    sum_to_pay *= 0.9

print(sum_to_pay)
