class Payment:
    def __init__(self, paymentId = None, paymentDate = None, paymentAmount = None, clientId = None):
        self.__paymentId = paymentId
        self.__paymentDate = paymentDate
        self.__paymentAmount = paymentAmount
        self.__clientId = clientId

    # Accessors
    def get_paymentId(self):
        return self.__paymentId

    def get_paymentDate(self):
        return self.__paymentDate
    
    def get_paymentAmount(self):
        return self.__paymentAmount
    
    def get_clientId(self):
        return self.__clientId
    
    # Mutators
    def set_paymentId(self, paymentId):
        self.__paymentId = paymentId

    def set_paymentDate(self, paymentDate):
        self.__paymentDate = paymentDate
    
    def set_paymentAmount(self, paymentAmount):
        self.__paymentAmount = paymentAmount

    def set_clientId(self, clientId):
        self.__clientId = clientId

    # toString
    def __str__(self):
        return f"Payment(paymentId = {self.__paymentId}, paymentDate = {self.__paymentDate}, paymentAmount = {self.__paymentAmount}, clientId = {self.__clientId})"     
    