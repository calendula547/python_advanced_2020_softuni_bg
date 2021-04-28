count_of_input_lines = int(input())

unique_elements = set()
for _ in range(count_of_input_lines):
    line = input().split()
    #for i in range(len(line)):
    [unique_elements.add(line[i]) for i in range(len(line)) if line[i] not in unique_elements]
        #if line[i] not in unique_elements:
            #unique_elements.add(line[i])

[print(el) for el in unique_elements]
