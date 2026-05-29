class employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary  = salary
    
class developer(employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language
    
    def show(self):
        print(f"name= {self.name}")
        print(f"salary = {self.salary}")
        print(f"language = {self.language}")

d = developer("devesh", 4000, "python")

d.show()