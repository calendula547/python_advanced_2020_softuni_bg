from collections import deque


def water_dispenser():
    start_quantity = int(input())
    people = deque()
    while True:
        command = input()
        if command == "Start":
            break
        else:
            people.append(command)

    while True:
        command = input().split()
        if command[0] == "End":
            break
        elif command[0].isdigit():
            wanted_litters = int(command[0])
            if wanted_litters <= start_quantity:
                person = people.popleft()
                print(f"{person} got water")
                start_quantity -= wanted_litters
            else:
                print(f"{people.popleft()} must wait")
        elif command[0] == "refill":
            start_quantity += int(command[1])

    print(f"{start_quantity} liters left")


water_dispenser()