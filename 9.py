class Restaurant():
    """docstring for Restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("This restaurant's name is " + self.restaurant_name.title() + ".")
        print("Its cuisine's type is " + self.cuisine_type.title() + ".")

    def open_restaurant(self):
        print("This restaurant is opening.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment_number_served):
        self.number_served += increment_number_served


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

class User():
    def __init__(self, firstname, lastname, gender, age):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def describe_user(self):
        print("My name is " + self.firstname.title() + self.lastname.title() + ".")
        print("Gender: " + self.gender.title())
        print("Age: " + str(self.age))
        print("Login attempts number: " + str(self.login_attempts))

    def greet_user(self):
        print("Hi, I'm " + self.firstname.title() + self.lastname.title() + ". Nice to meet you.")

class Admin(User):
    def __init__(self, firstname, lastname, gender, age):
        super().__init__(firstname, lastname, gender, age)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("Administraor's privileges are:")
        for privilege in self.privileges:
            print(privilege.title())

test_admin = Admin('Chen', 'Su', 'male', 20)
test_admin.describe_user()
test_admin.show_privileges()
