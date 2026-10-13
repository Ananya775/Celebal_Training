# PROG 4

import random
import time

# Generate random numbers
def generate_numbers(n):
    return [random.randint(1, 100) for _ in range(n)]

# Check whether a number is prime
def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

# Remove prime numbers using prime-checking function
def remove_primes(numbers):
    return [num for num in numbers if not is_prime(num)]

# Remove prime numbers using a precomputed set
def remove_primes_optimized(numbers, prime_set):
    return [num for num in numbers if num not in prime_set]

# Precompute primes between 1 and 100
prime_set = {num for num in range(1, 101) if is_prime(num)}

sizes = [100, 10000, 100000]

for n in sizes:
    print(f"\nComputing execution time for list size: {n}")

    # Generate random numbers and measure time
    start = time.perf_counter()
    numbers = generate_numbers(n)
    generation_time = time.perf_counter() - start

    # Normal approach
    start = time.perf_counter()
    result = remove_primes(numbers)
    normal_time = time.perf_counter() - start

    # Optimized approach
    start = time.perf_counter()
    optimized_result = remove_primes_optimized(numbers, prime_set)
    optimized_time = time.perf_counter() - start

    print(f"Time taken to generate random numbers: {generation_time:.6f} seconds")
    print(f"Time taken to remove primes (normal): {normal_time:.6f} seconds")
    print(f"Time taken to remove primes (optimized): {optimized_time:.6f} seconds")
    print(f"Normal total execution time: {generation_time + normal_time:.6f} seconds")
    print(f"Optimized total execution time: {generation_time + optimized_time:.6f} seconds")
    print(f"Time saved: {normal_time - optimized_time:.6f} seconds")

    if optimized_time < normal_time:
        print("Optimization improved execution time.")
    elif optimized_time > normal_time:
        print("Optimization was slower for this run.")
    else:
        print("Both approaches took approximately the same time.")



# PROG 5
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
