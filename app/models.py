from flask_login import UserMixin

#** Esta clase verifica la informacion necesaria
class UserData():
    def __init__(self, username, password):
        self.username =username
        self.password = password

class UserModel(UserMixin):
    def __init__(self,user_data):
        """
        Keyword arguments: user data
        argument -- atributos de la clase user_data
        Return: return_description
        """

        self.id=user_data.username
        self.password=user_data.password