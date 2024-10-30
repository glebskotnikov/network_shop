import pytest
from rest_framework.permissions import AllowAny

from users.models import User, Product
from users.permissions import IsActiveEmployee
from users.views import ProductViewSet


@pytest.mark.django_db
def test_user_create_view_without_supplier(api_client, test_user_data):
    """
    Test the creation of a user without a supplier.
    """
    data = {**test_user_data, "role": "fa"}

    response = api_client.post("/users/users/", data, format="json")

    assert response.status_code == 201
    assert "user" in response.data
    assert "message" in response.data
    assert response.data["message"] == "User created successfully"
    assert User.objects.filter(email=data["email"]).exists()


@pytest.mark.django_db
def test_user_create_view_with_supplier(
    api_client, test_user_data, test_user_fa
):
    """
    Test the creation of a user with a supplier.
    """
    data = {**test_user_data, "role": "rc", "supplier": test_user_fa.id}

    response = api_client.post("/users/users/", data, format="json")

    assert response.status_code == 201
    assert "user" in response.data
    assert "message" in response.data
    assert response.data["message"] == "User created successfully"
    assert User.objects.filter(email=data["email"]).exists()
    assert User.objects.filter(supplier=data["supplier"]).exists()


@pytest.mark.django_db
def test_user_create_view_with_supplier_and_product(
    api_client, test_user_data, test_user_fa, test_product
):
    """
    Test the creation of a user with a supplier and a product.
    """
    data = {
        **test_user_data,
        "role": "rc",
        "supplier": test_user_fa.id,
        "existing_products": [test_product.id],
    }

    response = api_client.post("/users/users/", data, format="json")

    assert response.status_code == 201
    assert "user" in response.data
    assert "message" in response.data
    assert response.data["message"] == "User created successfully"
    assert User.objects.filter(email=data["email"]).exists()
    assert User.objects.filter(supplier=data["supplier"]).exists()
    assert Product.objects.filter(id=test_product.id).exists()
    assert User.objects.filter(products__in=[test_product.id]).exists()


@pytest.mark.django_db
def test_user_create_view_bad_request(api_client):
    """
    Test a bad request in user creation.
    """
    data = {"non_existent_field": "random_value"}
    response = api_client.post("/users/users/", data, format="json")

    assert response.status_code == 400


@pytest.mark.django_db
def test_user_update_view(api_client, test_user_rc, test_user_em):
    """
    Test the user update view.
    """
    api_client.force_authenticate(user=test_user_em)

    updated_data = {
        "email": "updatedemail@example.com",
        "name": "Updated User",
        "debt": 500,
    }
    response = api_client.patch(
        f"/users/users/{test_user_rc.id}/", updated_data
    )

    api_client.force_authenticate(user=None)

    assert response.status_code == 200

    updated_user = User.objects.get(id=test_user_rc.id)
    assert updated_user.email == "updatedemail@example.com"
    assert updated_user.name == "Updated User"
    assert updated_user.debt == test_user_rc.debt


@pytest.mark.django_db
def test_product_view_set_create_permission(api_client, test_user_em):
    """
    Test the product view set creation permission.
    """
    view = ProductViewSet()

    view.action = "create"

    permissions = view.get_permissions()

    assert len(permissions) == 1
    assert isinstance(permissions[0], AllowAny)


@pytest.mark.django_db
def test_product_view_set_other_permission(api_client, test_user_em):
    """
    Test the product view set retrieve permission.
    """
    view = ProductViewSet()

    view.action = "retrieve"

    permissions = view.get_permissions()

    assert len(permissions) == 1
    assert isinstance(permissions[0], IsActiveEmployee)
