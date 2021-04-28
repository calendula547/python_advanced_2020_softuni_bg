from collections import deque

petrol_pumps_count = int(input())
pumps_info = deque()
fuel = 0
winner_stations = []
for i in range(0, petrol_pumps_count):
    fuel_kilos_info = [int(x) for x in input().split()]
    pumps_info.append(fuel_kilos_info)

for i in range(len(pumps_info)):
    current_station = pumps_info.popleft()
    fuel = fuel + current_station[0] - current_station[1]
    if fuel < 0:
        pumps_info.append(current_station)
        fuel = 0
        winner_stations = []
    else:
        winner_stations.append(i)
        pumps_info.append(current_station)
if len(winner_stations) != 0:
    print(winner_stations[0])





