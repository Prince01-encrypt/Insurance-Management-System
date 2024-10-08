class Policy :
    def __init__(self, policyId = None, policyName = None, premiumAmount = None, coverageAmount = None):
        self.__policyId = policyId
        self.__policyName = policyName
        self.__premiumAmount = premiumAmount
        self.__coverageAmount = coverageAmount

    # Accessors
    def get_policyId(self):
        return self.__policyId
    
    def get_policyName(self):
        return self.__policyName
    
    def get_premiumAmount(self):
        return self.__premiumAmount
    
    def get_coverageAmount(self):
        return self.__coverageAmount

    # Mutators
    def set_policyId(self, policyId):
        self.__policyId = policyId

    def set_policyName(self, policyName):
        self.__policyName = policyName

    def set_premiumAmount(self, premiumAmount):
        self.__premiumAmount = premiumAmount

    def set_coverageAmount(self, coverageAmount):
        self.__coverageAmount = coverageAmount

    # __str__ method for string representation
    def __str__(self):
        return f"Policy (policyId = {self.__policyId}, policyName = {self.__policyName}, premiumAmount = {self.__premiumAmount}, coverageAmount = {self.__coverageAmount})"
