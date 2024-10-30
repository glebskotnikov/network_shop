from django.core import management
from users.models import User
import pytest


@pytest.mark.django_db
def test_create_admin_command():
    """
    Test the creation of an admin user through the 'csu' management command.
    """
    management.call_command("csu")
    user = User.objects.get(email="admin@yandex.ru")
    assert user.name == "Admin"
    assert user.country == "Brazil"
    assert user.city == "Rio"
    assert user.street == "Avenida Vieira Souto"
    assert user.house_number == "13"
    assert user.role == "a"
    assert user.is_superuser is True
    assert user.is_staff is True
    assert user.is_active is True
    assert user.check_password("123qwe456rty") is True
