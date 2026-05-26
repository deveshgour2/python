line = 1
with open("file_handling/file1.txt") as f:
    for lines in f:
        data = f.readlines()
        print(data)