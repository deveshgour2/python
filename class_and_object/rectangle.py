class rectangle:
    def area(self, length , breadth):
       return (length * breadth)
    
    def perimeter(self, length , breadth):
        return (2*(length + breadth))
    
r = rectangle()
print(f"area = {r.area(2, 5 )}")
print(f"perimeter = {r.perimeter(2, 5)}")
