from rest_framework import serializers


def validate_supplier_role(supplier_role, user_role):
    allowed_supplier_map = {
        "fa": [],
        "em": [],
        "rc": ["fa", "rc"],
        "ie": ["fa", "rc", "ie"],
    }

    allowed_suppliers = allowed_supplier_map.get(user_role.lower())

    if supplier_role.lower() not in allowed_suppliers:
        raise serializers.ValidationError(
            f"{user_role} can only have {allowed_suppliers} as a supplier"
        )


def validate_admin_role(role):
    if role.lower() == "a":
        raise serializers.ValidationError("Users cannot register as admin")
    return role
