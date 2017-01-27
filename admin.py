from user import User

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']


    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege.title())


class Admin(User):
    def __init__(self, firstname, lastname, gender, age):
        super().__init__(firstname, lastname, gender, age)
        self.privileges = Privileges()