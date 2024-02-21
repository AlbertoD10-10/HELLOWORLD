import factories
from .models import Product 


class ProductFactory(factories.django.DjangoModelFactory): 
    class Meta: 
        model = Product 
    name = factories.Faker('company') 
    price = factories.Faker('random_int', min=200, max=9000) 