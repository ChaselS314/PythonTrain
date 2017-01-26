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

guoshen_restaurant = Restaurant('guo shen', 'ma la tang')
guoshen_restaurant.describe_restaurant()

chuancaiguan_restaurant = Restaurant('chuan cai guan', 'chuan cai')
chuancaiguan_restaurant.describe_restaurant()

hujin_restaurant = Restaurant('hu jin jiu lou', 'hu bei cai')
hujin_restaurant.describe_restaurant()

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

suchen_user = User('Chen', 'Su', 'male', 20)
suxin_user = User('Xin', 'Su', 'female', 10)
yoyo_user = User('Yoyo', 'Huang', 'female', 22)

suchen_user.describe_user()
suxin_user.describe_user()
yoyo_user.describe_user()

suchen_user.greet_user()
suxin_user.greet_user()
yoyo_user.greet_user()

restaurant = Restaurant('hong ding dou lao', 'huoguo')
restaurant.describe_restaurant()
print("It have served " + str(restaurant.number_served) + " customers.")
restaurant.set_number_served(100)
print("It have served " + str(restaurant.number_served) + " customers.")
restaurant.increment_number_served(50)
print("It have served " + str(restaurant.number_served) + " customers.")

suchen_user.increment_login_attempts()
suchen_user.increment_login_attempts()
suchen_user.describe_user()
suchen_user.reset_login_attempts()
suchen_user.describe_user()
