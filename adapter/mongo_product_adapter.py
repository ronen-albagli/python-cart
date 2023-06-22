from ports.product_mongo_port import ProductMongoPort

class ProductMongoGateway(ProductMongoPort):
    def __init__(self, mongoProduct):
        self.mongoProductCollection = mongoProduct
        
    def store(self, product_data):
        self.mongoProductCollection.insert_one(product_data);

    def get_by_id(self, id):
        return self.mongoProductCollection.find_one({'productId': id})
    
    