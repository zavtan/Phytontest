# TODO решите задачу
def task() -> float:
    ...


print(task())
import json

with open("data.json", "r") as file:
    data = json.load(file)

sum_of_products = 0
for ip in data:
    product = ip["score"] * ip["weight"]
    sum_of_products += product

print("Sum of products: {:.3f}".format(sum_of_products))