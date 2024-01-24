from collections import deque

chocolates = deque(int(x) for x in input().split(', '))
cups_of_milks = deque(int(x) for x in input().split(', '))

milkshakes = 0

while milkshakes != 5 and chocolates and cups_of_milks:
    chocolate = chocolates.pop()
    cup_of_milk = cups_of_milks.popleft()

    if chocolate <= 0 and cup_of_milk <0:
        continue
    elif chocolate <= 0:
        cups_of_milks.appendleft(cup_of_milk)
        continue
    elif cup_of_milk <= 0:
        chocolates.append(chocolate)
        continue

    if cup_of_milk == chocolate:
        milkshakes += 1
    else:
        cups_of_milks.append(cup_of_milk)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed! ")
else:
    print(f"Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(x) for x in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(x) for x in cups_of_milks) or 'empty'}")
