n = int(input())
unique_usernames = set()
[unique_usernames.add(input()) for _ in range(n)]
[print(name) for name in unique_usernames]