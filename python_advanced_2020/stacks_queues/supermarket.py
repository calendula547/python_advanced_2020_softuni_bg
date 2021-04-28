from collections import deque

clients = deque()
command = input().split()
while command[0] != "End":
    if command[0] != "Paid":
        clients.append(command[0])
    elif command[0] == "Paid":
        for i in range(len(clients)):
            print(clients.popleft())

    command = input().split()
print(f"{len(clients)} people remaining.")