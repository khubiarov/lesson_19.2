from django.core.management.base import BaseCommand
from catalog.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Product.objects.all().delete()

        products_list = [
            {'name': 'tester', 'price': 800, 'description': 'Device for electronics', 'category_id': 6},
            {'name': 'Big_mak', 'price': 100, 'description': 'meal', 'category_id': 7},
            {'name': 'hummer', 'price': 350, 'description': 'for testing', 'category_id': 6},
            {'name': 'Dos 6.22', 'price': 35, 'description': 'Latest version of microsoft dos', 'category_id': 5},
            {'name': 'Widows 3.11', 'price': 45, 'description': 'windows for 80386 computer ', 'category_id': 5},
            {'name': 'cheescake', 'price': 150, 'description': 'sweet food for coffe-breake ', 'category_id': 7},
            # {'name': 'tester', 'price': 800, 'description': 'for testing', 'category_id': 5},
            # {'name': 'tester', 'price': 800, 'description': 'for testing', 'category_id': 5},
        ]

        for item in products_list:
            Product.objects.create(**item)
