from usecase.base import BaseUseCase
from ports.catalog_stripe_port import MongoCatalogPort
from typing import Type, TypeVar

MongoCatalogPort = TypeVar('MongoCatalogPort', bound=MongoCatalogPort)

class UseCaseConfig(TypedDict):
    mongoCatalog: Type[MongoCatalogPort]

class CreateCatalogUseCase(BaseUseCase):
    config: UseCaseConfig
    
    def __init__(self, usecaseConfig: UseCaseConfig):
        self.config = usecaseConfig
        
    def execute(self, catalog_data):
        self.config.mongoCatalog.store(catalog_data=catalog_data);
        