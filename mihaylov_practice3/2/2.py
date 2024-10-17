def write_and_read_file(filename, content):

    with open(filename, 'w') as file:
        file.write(content)

    with open(filename, 'r') as file:
        file_content = file.read()
    
    return file_content

filename = 'example.txt'
content = 'Hello, World!'
result = write_and_read_file(filename, content)
print(result)  