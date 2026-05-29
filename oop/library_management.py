class library:
    def display_info(self):
        pass        

class book(library):
    def __init__(self, title):
        self.title = title
    
    def display_info(self):
        print(f"book = {self.title}")

class magazine(library):
    def __init__(self, title):
        self.title = title
    
    def display_info(self):
        print(f"magazine = {self.title}")
    

lib = [book("python"), magazine("know yourself")]

for l in lib:
    l.display_info()