def age_assignment(*args, **kwargs):
    result_dict = {}
    for arg in args:
        result_dict[arg] = kwargs[arg[0]]
    return result_dict


print(age_assignment("Peter", "George", G=26, P=19))