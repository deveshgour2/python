with open("file_handling/file.txt") as f:
    content = f.read()

with open("file_handling/file1.txt", "w") as f:
    f.write(content)