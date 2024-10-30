import pytest
from django.contrib.admin import AdminSite
from django.urls import reverse

from users.admin import UserAdmin, ProductAdmin
from users.models import User, Product


@pytest.mark.django_db
class TestUserAdmin:
    """
    Container for all UserAdmin model tests.
    """

    def test_role_type(self, test_user_rc):
        """
        Test the role type feature in the UserAdmin page.
        """
        site = AdminSite()
        admin = UserAdmin(model=User, admin_site=site)

        assert admin.role_type(test_user_rc) == test_user_rc.role

    def test_supplier_link(self, test_user_with_s, test_user_fa):
        """
        Test the supplier link feature in the UserAdmin page.
        """
        site = AdminSite()
        admin = UserAdmin(model=User, admin_site=site)
        expected_url = reverse(
            "admin:users_user_change", args=[test_user_fa.id]
        )

        assert expected_url in admin.supplier_link(test_user_with_s)
        assert admin.supplier_link(test_user_fa) == "No supplier"

    def test_clear_debt(self, test_user_with_debt):
        """
        Test the 'Clear Debt' admin action in the UserAdmin page.
        """
        site = AdminSite()
        admin = UserAdmin(model=User, admin_site=site)
        queryset = User.objects.filter(id=test_user_with_debt.id)
        admin.clear_debt(None, queryset)
        test_user_with_debt.refresh_from_db()

        assert test_user_with_debt.debt == 0


@pytest.mark.django_db
class TestProductAdmin:
    """
    Container for all ProductAdmin model tests.
    """

    def test_list_display(self, test_product):
        """
        Test the list display configuration for ProductAdmin.
        """
        site = AdminSite()
        admin = ProductAdmin(model=Product, admin_site=site)

        assert admin.list_display == ("id", "name", "model", "release_date")
