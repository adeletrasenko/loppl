def print_params(a=1, b='строка', c=True):
    print(a, b, c)


#print_params()
value_list = (1,2,3)
value_dict = {"a": 1, "b":'строка', "c": True}

#print_params(*value_list)
#print_params(**value_dict)


def append_to_list(item, list_my=None):
    if list_my is None:
        list_my = []
    list_my.append(item)


    print(list_my)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)