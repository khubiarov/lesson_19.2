from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.create(name='Food', id=1)
        Category.objects.create(name='Tools', id=2)
        Category.objects.create(name='Softwere', id=3)
        products_list = [
            {'name': 'tester', 'price': 800, 'description': 'Device for electronics', 'category_id': 2},
            {'name': 'Big_mak', 'price': 100, 'description': 'meal', 'category_id': 1},
            {'name': 'hummer', 'price': 350, 'description': 'for testing', 'category_id': 2},
            {'name': 'Dos 6.22', 'price': 35, 'description': 'Latest version of microsoft dos', 'category_id': 3},
            {'name': 'Widows 3.11', 'price': 45, 'description': 'windows for 80386 computer ', 'category_id': 3},
            {'name': 'cheescake', 'price': 150, 'description': 'sweet food for coffe-breake ', 'category_id': 1},
            # {'name': 'tester', 'price': 800, 'description': 'for testing', 'category_id': 5},
            # {'name': 'tester', 'price': 800, 'description': 'for testing', 'category_id': 5},
        ]

        for item in products_list:
            Product.objects.create(**item)
