def read_from_file(name) : 
    with open(name) as file : 
        content = file.read()
    return  content

file_content = read_from_file('pets.txt')
content_words = len(file_content.split())

print(content_words)