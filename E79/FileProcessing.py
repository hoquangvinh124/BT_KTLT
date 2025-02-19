def read_data(path):
    arr_number = []
    with open(path, 'r') as file:
        for line in file:
            data = line.strip()
            arr = data.split(',')
            arr_number.append(arr)
    return arr_number

def write_data(path, data):
    with open(path, 'a') as file:
        file.writelines(data)
        file.writelines("\n")
