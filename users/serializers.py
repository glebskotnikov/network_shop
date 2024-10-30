from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import Product, User
from users.validators import validate_admin_role, validate_supplier_role


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    existing_products = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Product.objects.all(),
        required=False,
        source="products",
    )

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "name",
            "country",
            "city",
            "street",
            "house_number",
            "role",
            "supplier",
            "existing_products",
        )
        read_only_fields = ("debt",)


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(min_length=8, write_only=True)

    role = serializers.ChoiceField(
        choices=User.ROLE_CHOICES, validators=[validate_admin_role]
    )

    supplier = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True, required=False
    )

    existing_products = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Product.objects.all(), write_only=True
    )

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "name",
            "country",
            "city",
            "street",
            "house_number",
            "role",
            "supplier",
            "existing_products",
        )

    def create(self, validated_data):
        password = validated_data.pop("password")
        existing_products_data = validated_data.pop("existing_products", [])
        supplier = validated_data.pop("supplier", None)

        user = User.objects.create(**validated_data)
        if supplier is not None:
            user.supplier = supplier
        user.set_password(password)
        user.save()

        for product_data in existing_products_data:
            user.products.add(product_data)

        user.save()

        return UserSerializer(user).data

    def validate(self, attrs):
        role = attrs.get("role")
        supplier = attrs.get("supplier")

        if supplier:
            supplier_role = supplier.role

            validate_supplier_role(supplier_role, role)

        return attrs
