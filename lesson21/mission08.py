def create_dict(data, template):
    if isinstance(data, dict):
        return data
    elif isinstance(data, int) or isinstance(data, float) or isinstance(data, str):
        template[data] = data
        return template
    else:
        pass


def data_preparation(old_list):
    new_list = []
    for i_element in old_list:
        point = (create_dict(i_element, template={}))
        if point:
            new_list.append(point)
    return new_list


data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 2323]

data = data_preparation(data)

print(data)
