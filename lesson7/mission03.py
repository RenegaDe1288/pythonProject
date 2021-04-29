win = 0
for tickets in 345, 19, 87, 1020, 421:
    if tickets//1000 == 0 and tickets%5 == 0:
        win += 1
        print(tickets)
print(win)