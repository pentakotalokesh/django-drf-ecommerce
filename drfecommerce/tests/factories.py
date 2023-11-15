import factory

from drfecommerce.product.models import Brand, Category, Product


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.sequence(lambda n: "Category_%d" % n)


class BrandFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Brand

    name = factory.sequence(lambda n: "Brand_%d" % n)


# As we need to test the product but it has relationships with the other two entitys
# There is an subFactory option in the factoryboy


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.sequence(lambda n: "Product_%d" % n)
    description = "The First Product"
    is_digital = True
    brand = factory.SubFactory(BrandFactory)
    category = factory.SubFactory(CategoryFactory)
