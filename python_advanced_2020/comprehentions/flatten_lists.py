num_list = [el.split(" ") for el in input().split('|')][::-1]
flatten_list = [x for sublist in num_list for x in sublist]
filtered_list = [el for el in flatten_list if el != ""]
print(" ".join(filtered_list))






