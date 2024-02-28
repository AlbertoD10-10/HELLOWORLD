import factories
from .models import Product 
from .models import Comment


class ProductFactory(factories.django.DjangoModelFactory): 
    class Meta: 
        model = Product 
    name = factories.Faker('company') 
    price = factories.Faker('random_int', min=200, max=9000) 

class CommentFactory(factories.django.DjangoModelFactory):
    class Meta:
        model = Comment
    description = factories.Faker('company')
    product_id = factories.Faker('random_int', min=200, max=9000)