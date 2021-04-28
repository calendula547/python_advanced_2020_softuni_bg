countries = input().split(", ")
capitals = input().split(", ")
result_dict = {k:v for (k,v) in zip(countries, capitals)}
for k,v in result_dict.items():
    print(f"{k} -> {v}")