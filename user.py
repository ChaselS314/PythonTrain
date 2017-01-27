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
