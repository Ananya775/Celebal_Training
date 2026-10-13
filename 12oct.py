
import random

HOUSEHOLD_GST = 0.05
PROCESSED_FOOD_GST = 0.12

items = [
    "Banana", "Masala", "Tomato", "Rice", "Soap",
    "Milk", "Bread", "Shampoo", "Biscuits", "Oil",
    "Sugar", "Tea", "Detergent", "Cheese", "Juice"
]

prices = [
    15, 200, 10, 60, 40,
    30, 35, 120, 25, 150,
    45, 100, 80, 90, 50
]

gst_category = [
    HOUSEHOLD_GST, PROCESSED_FOOD_GST, HOUSEHOLD_GST,
    PROCESSED_FOOD_GST, HOUSEHOLD_GST,
    PROCESSED_FOOD_GST, PROCESSED_FOOD_GST, HOUSEHOLD_GST,
    PROCESSED_FOOD_GST, PROCESSED_FOOD_GST,
    PROCESSED_FOOD_GST, PROCESSED_FOOD_GST, HOUSEHOLD_GST,
    PROCESSED_FOOD_GST, PROCESSED_FOOD_GST
]

buyer = input("Enter the buyer name: ")

selected_items = random.sample(range(len(items)), 3)

total = 0
gst_total = 0

print("\nRetail Invoicing App")
print("----------------------------------------")
print("Buyer Name:", buyer)
print("----------------------------------------")
print("| {:<15} | {:^5} | {:>10} |".format("Item", "Qty", "Price"))
print("----------------------------------------")

for i in selected_items:
    quantity = random.randint(1, 5)

    item_total = prices[i] * quantity
    item_gst = item_total * gst_category[i]

    total += item_total
    gst_total += item_gst

    print("| {:<15} | {:^5} | {:>10.2f} |".format(
        items[i], quantity, item_total
    ))

print("----------------------------------------")
print("Total                         Rs {:.2f}".format(total))
print("GST                           Rs {:.2f}".format(gst_total))
print("----------------------------------------")
print("Total Billing                 Rs {:.2f}".format(
    total + gst_total
))
print("----------------------------------------")
