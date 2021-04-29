for number in range(10, 100):
    if number == 3 * ((number % 10) * (number // 10)):
        print(number)
