def calculate_structure_sum(args):
    a = 0
    if isinstance(args, int):
        a += args
    elif isinstance(args, str):
        a += len(args)
    elif isinstance(args, dict):
        dict_f = args
        for k in range(0, len(dict_f)):
            a += len(str(list(dict_f.keys())[k])) + list(dict_f.values())[k]
    else:
        if isinstance(args, set):
            args = list(args)
        for j in range(0, len(args)):
            a += calculate_structure_sum(args[j])
    return a


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(data_structure)
result = 0
for i in range(0, len(data_structure)):
    result += calculate_structure_sum(data_structure[i])
print(result)
