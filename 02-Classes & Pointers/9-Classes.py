class Cookie:
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    # Getter of the color property of the object
    def get_color(self):
        return self.color

    # Setter of the color property of the object
    def set_color(self,color):
        self.color = color

    # Getter of the brand property of the object
    def get_brand(self):
        return self.brand
    
    # Setter of the brand property of the object
    def set_brand(self, brand):
        self.brand = brand



cookie_one = Cookie('green', 'Oreo')        # Creation of the object
cookie_two = Cookie('blue', 'Chips Ahoy')   # Creation of the object

print('Cookie one is a', cookie_one.get_color(), cookie_one.get_brand())
print('Cookie two is a', cookie_two.get_color(), cookie_two.get_brand())

cookie_one.set_color('orange')

print('\nCookie one is now a', cookie_one.get_color(), cookie_one.get_brand())
print('Cookie two is still a', cookie_two.get_color(), cookie_two.get_brand())


    
