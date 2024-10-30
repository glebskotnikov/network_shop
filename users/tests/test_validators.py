import pytest
from rest_framework import serializers

from users.validators import validate_supplier_role, validate_admin_role


def test_validate_supplier_role_raises_error():
    """
    Test if an error is raised when validating invalid supplier role.
    """
    user_role = "fa"
    supplier_role = "rc"

    with pytest.raises(serializers.ValidationError) as excinfo:
        validate_supplier_role(supplier_role, user_role)

    error_message = excinfo.value.detail[0]

    assert error_message == f"{user_role} can only have {[]} as a supplier"


def test_validate_admin_role_raises_error():
    """
    Test if an error is raised when validating invalid admin role.
    """
    role = "a"

    with pytest.raises(serializers.ValidationError) as excinfo:
        validate_admin_role(role)

    error_message = excinfo.value.detail[0]

    assert error_message == "Users cannot register as admin"


def test_validate_supplier_role_no_error():
    """
    Test if no error is raised when validating valid supplier role.
    """
    user_role = "rc"
    supplier_role = "fa"

    try:
        validate_supplier_role(supplier_role, user_role)
    except serializers.ValidationError:
        pytest.fail(
            f"Unexpected ValidationError with {user_role} and {supplier_role}"
        )


def test_validate_admin_role_no_error():
    """
    Test if no error is raised when validating a non-admin role.
    """
    role = "user_role"

    try:
        validate_admin_role(role)
    except serializers.ValidationError:
        pytest.fail(f"Unexpected ValidationError with role {role}")
