from collections import deque

quantity = int(input())
orders = deque([int(x) for x in input().split()])


if orders:
    print(max(orders))
while orders:
    current_order = orders.popleft()
    if quantity >= current_order:
        quantity -= current_order

    else:
        orders.appendleft(current_order)
        break
if len(orders) == 0:
    print("Orders complete")
else:
    print(f"Orders left:", end=" ")
    for i in range(len(orders)):
        print(orders[i], end=" ")


