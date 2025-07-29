import factory
from faker import Faker
from django.conf import settings
from everycheese.cheeses.models import Cheese

fake = Faker()

class CheeseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cheese

    name        = factory.LazyAttribute(lambda _: fake.unique.word().title())
    description = factory.LazyAttribute(lambda _: fake.text(80))
    country     = "CO"
    firmness    = "hard"
    added_by    = factory.SubFactory("users.tests.factories.UserFactory")