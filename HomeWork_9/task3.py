# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

input_file = "test_file/task_3.txt"

with open(input_file, 'r') as file:
    lines = file.read().splitlines()

purchases = []
current_purchase = []
for line in lines:
    if line.strip():
        current_purchase.append(int(line))
    else:
        if current_purchase:
            purchases.append(current_purchase)
            current_purchase = []

purchase_sums = []
for purchase in purchases:
    purchase_sum = sum(purchase)
    purchase_sums.append(purchase_sum)

purchase_sums.sort(reverse=True)
three_most_expensive_purchases = sum(purchase_sums[:3])

assert three_most_expensive_purchases == 202346