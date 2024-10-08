class User :
    def __init__(self, userId = None, username = None, password = None, role = None) :
        self.__userId = userId
        self.__username = username
        self.__password = password
        self.__role = role

    # Accessors
    def get_userId(self) :
        return self.__userId
    
    def get_username(self):
        return self.__username
    
    def get_password(self):
        return self.__password
    
    def get_role(self):
        return self.__role
    
    # Mutators
    def set_userId(self, userId) :
        self.__userId = userId

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_role(self, role):
        self.__role = role

    # __str__ method for string representation
    def __str__(self) :
        return f"User(userId = {self.__userId}, username = {self.__username}, password = ****** role = {self.__role})"
