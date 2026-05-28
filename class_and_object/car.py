class car:
    def brand(self, brand ):
        return brand 
    
    def model(self, model):
        return model
    
c = car()
print(f"brand = {c.brand("tata")}")
print(f"model = {c.model("sierra")}")