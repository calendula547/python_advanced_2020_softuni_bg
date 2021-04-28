from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets_stack = list(map(int, (input().split())))
locks = deque(map(int, (input().split())))
intelligence = int(input())


