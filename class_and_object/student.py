class student:
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

s1 = student("Devesh" , 88)
s2 = student("sanjay" , 90)

print(f'''name = {s1.name}
marks = {s1.marks}''')

print(f'''name = {s2.name}
marks = {s2.marks}''')