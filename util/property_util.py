class PropertyUtil :
    
    @staticmethod
    def getConnectionString() :
        return (
            'Driver={SQL Server};'
            'Server=PRINCE\\SQLEXPRESS;'  
            'Database=InsuranceManagementSystem;'
            'Trusted_Connection=yes;'
        )