import pytest  # Connects our tests with our database
from everycheese.cheeses.tests.factories import CheeseFactory

pytestmark = pytest.mark.django_db


def test___str__():
    cheese = CheeseFactory()
    assert cheese.__str__() == cheese.name
    assert str(cheese) == cheese.name
