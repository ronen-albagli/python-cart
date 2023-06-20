
from ports.subscription_port import SubscriptionPort

class Create_subscription_use_case():
    config: SubscriptionPort
    def __init__(self, usecaseConfig: SubscriptionPort):
        self.config = usecaseConfig
    
    
    def execute(self, subscription_input):
        self.config.store(subscription_input)