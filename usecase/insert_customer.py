
from ports.customer_port import CustomerPort

class Create_customer_use_case():
    config: CustomerPort
    def __init__(self, usecaseConfig: CustomerPort):
        self.config = usecaseConfig
    
    
    def execute(self, customerData):
        print('customerData',customerData)
        return self.config.store(customerData.get('email'), customerData.get('source'))