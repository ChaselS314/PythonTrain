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