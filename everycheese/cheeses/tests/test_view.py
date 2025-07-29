import pytest
from django.urls import reverse
from everycheese.cheeses.models import Cheese
from everycheese.cheeses.tests.factories import CheeseFactory

@pytest.mark.django_db
def test_cheese_list_view_authenticated(client, django_user_model):
    user = django_user_model.objects.create_user(username="user1", password="pass")
    client.login(username="user1", password="pass")

    Cheese.objects.create(name="Brie", description="French cheese", added_by=user)

    response = client.get(reverse("cheese_list"))
    assert response.status_code == 200
    assert b"Brie" in response.content

@pytest.mark.django_db
def test_cheese_list_shows_factory_data(client, django_user_model):
    user = django_user_model.objects.create_user("u","u@example.com","pass")
    client.login(username="u", password="pass")

    # Creamos 3 quesos de prueba
    cheeses = CheeseFactory.create_batch(3, added_by=user)

    response = client.get(reverse("cheeses:list"))
    assert response.status_code == 200
    for cheese in cheeses:
        assert cheese.name.encode() in response.content