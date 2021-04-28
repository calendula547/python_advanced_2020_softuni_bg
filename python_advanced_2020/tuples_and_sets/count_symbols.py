def count_letters(text):
    letters_count_dict = {}
    for letter in text:
        if letter not in letters_count_dict:
            letters_count_dict[letter] = 0
        letters_count_dict[letter] += 1
    return letters_count_dict


def print_result(letters_dict):
    for k, v in sorted(letters_dict.items()):
        print(f'{k}: {v} time/s')


result = count_letters(input())
print_result(result)