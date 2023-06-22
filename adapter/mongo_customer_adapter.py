from ports.customer_mongo_port import CustomerMongoPort

class CustomerMongoGateway(CustomerMongoPort):
    def __init__(self, mongoCustomer):
        self.mongoCustomerCollection = mongoCustomer
        
    def store(self, customerId, accountId ):
        self.mongoCustomerCollection.insert_one({'customerId': customerId, 'accountId': accountId});
        
    def findByAccountId(self, accountId):
        return self.mongoCustomerCollection.find_one({'accountId': accountId})

        
    
    