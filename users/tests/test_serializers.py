import pytest
from users.serializers import (
    UserSerializer,
    UserRegisterSerializer,
    ProductSerializer,
)


@pytest.mark.django_db
def test_user_serializer(test_user_fa):
    """
    Test UserSerializer.
    """
    serializer = UserSerializer(instance=test_user_fa)
    assert serializer.data["email"] == test_user_fa.email
    assert serializer.data["name"] == test_user_fa.name


@pytest.mark.django_db
def test_user_register_serializer(test_user_ie, test_product):
    """
    Test UserRegisterSerializer.
    """
    data = {
        "email": "new_user@gmail.com",
        "password": "password1234",
        "name": "New User",
        "role": "ie",
        "supplier": test_user_ie.id,
        "existing_products": [test_product.id],
    }
    serializer = UserRegisterSerializer(data=data)
    assert serializer.is_valid()
    assert isinstance(serializer.save(), dict)


@pytest.mark.django_db
def test_product_serializer(test_product):
    """
    Test ProductSerializer.
    """
    serializer = ProductSerializer(instance=test_product)
    assert serializer.data["name"] == test_product.name
    assert serializer.data["model"] == test_product.model
