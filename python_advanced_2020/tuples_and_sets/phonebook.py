phonebook_dict = {}
count = None

while True:
    name_and_number = (input().split("-"))
    name = name_and_number[0]
    if name.isdigit():
        count = int(name)
        break
    number = name_and_number[1]
    if name not in phonebook_dict:
        phonebook_dict[name] = number
    phonebook_dict[name] = number

for i in range(count):
    name_for_search = input()
    if name_for_search in phonebook_dict.keys():
        print(f"{name_for_search} -> {phonebook_dict[name_for_search]}")
    else:
        print(f"Contact {name_for_search} does not exist.")








