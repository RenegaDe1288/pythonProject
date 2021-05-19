import random

original_prices = [random.randint(-20, 20) for num in range(random.randint(5, 8))]

new_prices = [0 if num < 0 else num for num in original_prices]
print(original_prices)
print(new_prices)
print("Мы потеряли: ", abs(sum(original_prices) - sum(new_prices)))
