from restaurant import Restaurant
from admin import Admin

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def describe_flavors(self):
        for flavor in self.flavors:
            print(flavor.title())

my_icecreamstand = IceCreamStand('chayin', 'ice cream', ['coffee', 'coco', 'green tea'])
my_icecreamstand.describe_restaurant()
my_icecreamstand.describe_flavors()



test_admin = Admin('Chen', 'Su', 'male', 20)
test_admin.describe_user()
test_admin.privileges.show_privileges()