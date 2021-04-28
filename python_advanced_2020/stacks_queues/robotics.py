from collections import deque


def add_time(h, m, s):
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        h = 0
    return h, m, s


robots = list(input().split(";"))
available_robots = deque()
waiting_robots = deque()
start_time = input().split(":")
products = deque()
robots_dict = {}
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

start_hour = int(start_time[0])
start_minute = int(start_time[1])
start_seconds = int(start_time[2])
#print(add_time(start_hour, start_minute, start_seconds))
#print(products)
for robot in robots:
    robot_name, robot_time = robot.split("-")
    available_robots.append([robot_name, robot_time])
    robots_dict[robot_name] = int(robot_time)
#start_time = add_time(start_hour, start_minute, start_seconds)

while products:
    start_time = add_time(start_hour, start_minute, start_seconds)
    current_product = products.popleft()
    if available_robots:
        current_robot = available_robots.popleft()
        print(f"{current_robot[0]} - {current_product} [{start_time[0]:02d}:{start_time[1]:02d}:{start_time[2]:02d}]")
        waiting_robots.append(current_robot)
    else:
        products.append(current_product)

    if waiting_robots:
        for robot in waiting_robots:
            robot_name = robot[0]
            time = int(robot[1])
            time -= 1

            if time <= 0:
                available_robots.append([robot_name, robots_dict[robot_name]])

        waiting_robots = [r for r in waiting_robots if int(r[1]) > 0]

    start_seconds += 1




