def create_string_from_dict(index_dict):
    char_at_index = {}

    for char, positions in index_dict.items():
        for pos in positions:
            char_at_index[pos] = char
  

    highest_index = -1
    if char_at_index:
        highest_index = max(char_at_index.keys())

    result_list = []
    for i in range(highest_index + 1):
        result_list.append(char_at_index.get(i, " "))

    result_string = "".join(result_list)

    return result_string


d = eval(input())
print(create_string_from_dict(d))
