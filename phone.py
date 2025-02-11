class Phone:
    def __init__(self, model, color, price):
        self.model = model
        self.color = color
        self.price = price

    def get_model(self):
        return f"The phone model is {self.model}"

    def get_color(self):
        return f"The phone color is {self.color}"

    def get_price(self):
        return f"The phone price is {self.price}"


phone = Phone("OnePlus", "Blue", 30000)


print(phone.get_model()) 
print(phone.get_price()) 
print(phone.get_color())  
