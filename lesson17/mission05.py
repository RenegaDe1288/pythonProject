original_prices = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

new_prces = [0 if num < 0 else num for num in original_prices]

print(new_prces)
