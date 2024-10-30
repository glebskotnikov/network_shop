import pytest
from rest_framework.test import APIClient
from users.models import User, Product


# pytest fixture for API client
@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def test_user_data(db):
    return {
        "email": "test_user_data@email.com",
        "password": "testpassword",
        "name": "test_user_data",
        "country": "Test Country",
        "city": "Test City",
        "street": "Test Street",
        "house_number": "123",
        "existing_products": [],
    }


# pytest fixture for user
@pytest.fixture
def test_user_fa():
    return User.objects.create(
        email="test_user_fa@gmail.com", name="Test user factory", role="fa"
    )


@pytest.fixture
def test_user_rc():
    return User.objects.create(
        email="test_user_rc@gmail.com", name="Test user retailchain", role="rc"
    )


@pytest.fixture
def test_user_ie():
    return User.objects.create(
        email="test_user_ie@gmail.com",
        name="Test user individual entrepreneur",
        role="ie",
    )


@pytest.fixture
def test_user_em():
    return User.objects.create(
        email="test_user_em@gmail.com",
        name="Test user employee",
        role="em",
        is_active=True,
        is_staff=True,
    )


# @pytest.fixture
# def test_user_admin():
#     return User.objects.create(
#         email='test_user_a@gmail.com',
#         name='Test user Admin',
#         role='a',
#         is_active=True,
#         is_staff=True,
#         is_superuser=True
#     )


@pytest.fixture
def test_user_with_s(test_user_fa):
    return User.objects.create(
        email="test_user_with_s@gmail.com",
        name="Test user with supplier",
        role="rc",
        supplier=test_user_fa,
    )


@pytest.fixture
def test_user_with_debt(test_user_fa):
    return User.objects.create(
        email="test_user_with_debt@gmail.com",
        name="Test user with debt",
        role="rc",
        supplier=test_user_fa,
        debt=500.55,
    )


# pytest fixture for the product
@pytest.fixture
def test_product():
    return Product.objects.create(
        name="Test Product", model="Model001", release_date="2024-09-20"
    )
