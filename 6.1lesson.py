def calculate_structure_sum(data):
    if isinstance(data,(int,float)):
        return data
    if isinstance(data,str):
        return len(data)
    if isinstance(data,(tuple,list)):
        if len(data)==0:
            return 0
        return calculate_structure_sum(data[0])+calculate_structure_sum(data[1:])
    if isinstance(data,set):
        return calculate_structure_sum(list(data))
    if isinstance(data,dict):
        return calculate_structure_sum(list(data.items()))

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(calculate_structure_sum(data_structure))
