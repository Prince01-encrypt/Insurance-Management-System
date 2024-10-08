class Client:
    def __init__(self, clientId = None, clientName = None, contactInfo = None, policyId = None):
        self.__clientId = clientId
        self.__clientName = clientName
        self.__contactInfo = contactInfo
        self.__policyId = policyId

    # Accessors
    def get_clientId(self):
        return self.__clientId

    def get_clientName(self):
        return self.__clientName
    
    def get_contactInfo(self):
        return self.__contactInfo
    
    def get_policyId(self):
        return self.__policyId   
    
    # Mutators
    def set_clientId(self, clientId):
        self.__clientId = clientId

    def set_clientName(self, clientName):
        self.__clientName = clientName

    def set_contactInfo(self, contactInfo):
        self.__contactInfo = contactInfo

    def set_policyId(self, policyId):
        self.__policyId = policyId

    # __str__ method for string representation
    def __str__(self):
        return f"Client(clientId = {self.__clientId}, clientName = {self.__clientName}, contactInfo = {self.__contactInfo}, policyId = {self.__policyId})"   
