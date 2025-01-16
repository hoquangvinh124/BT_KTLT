ex = input("Vui long nhap url: ")

def split_components(url):
    after_split = url.split('/')
    protocol = after_split[0]
    hostname = after_split[2]
    directory = after_split[3]
    query_parameter_with_file_name = after_split[4].split('?', 1) if len(after_split) > 4 else ''
    file_name = query_parameter_with_file_name[0] if query_parameter_with_file_name else ''
    query_parameters = query_parameter_with_file_name[1] if len(query_parameter_with_file_name) > 1 else ''
    return (print(f'protocol: {protocol}'), print(f'hostname: {hostname}'), print(f'directory: {directory}')
            , print(f'file_name: {file_name}'), print(f'query_parameters: {query_parameters}'))

split_components(ex)





