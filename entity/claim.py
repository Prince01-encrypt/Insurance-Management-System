class Claim:
    def __init__(self, claimId = None, claimNumber = None, dateFiled = None, claimAmount = None, status = None, policyId = None, clientId = None) :  
        self.__claimId = claimId
        self.__claimNumber = claimNumber
        self.__dateFiled = dateFiled
        self.__claimAmount = claimAmount
        self.__status = status
        self.__policyId = policyId
        self.__clientId = clientId

    # Accessors
    def get_claimId(self):
        return self.__claimId

    def get_claimNumber(self):
        return self.__claimNumber
    
    def get_dateFiled(self):
        return self.__dateFiled
    
    def get_claimAmount(self):
        return self.__claimAmount
    
    def get_status(self):
        return self.__status
    
    def get_policyId(self):
        return self.__policyId
    
    def get_clientId(self):
        return self.__clientId
    
    # Mutators
    def set_claimId(self, claimId):
        self.__claimId = claimId

    def set_claimNumber(self, claimNumber):
        self.__claimNumber = claimNumber

    def set_dateFiled(self, dateFiled):
        self.__dateFiled = dateFiled

    def set_claimAmount(self, claimAmount):
        self.__claimAmount = claimAmount

    def set_status(self, status):
        self.__status = status

    def set_policyId(self, policyId):
        self.__policyId = policyId

    def set_clientId(self, clientId):
        self.__clientId = clientId

    # __str__ method for string representation
    def __str__(self):
        return (f"Claim(claimId = {self.__claimId}, claimNumber = {self.__claimNumber}, "
                f"dateFiled = {self.__dateFiled}, claimAmount = {self.__claimAmount}, "
                f"status = {self.__status}, policyId = {self.__policyId}, clientId = {self.__clientId})")
