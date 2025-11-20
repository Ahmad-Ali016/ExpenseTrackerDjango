from django.core.management.base import BaseCommand
from core.models import Category

class Command(BaseCommand):
    help = "Add default 15–20 categories to the database"

    def handle(self, *args, **kwargs):
        categories = [
            "Electronics",
            "Clothing",
            "Accessories",
            "Beauty & Personal Care",
            "Home Appliances",
            "Footwear",
            "Furniture",
            "Sports & Fitness",
            "Books",
            "Toys & Games",
            "Groceries",
            "Mobile Phones",
            "Laptops",
            "Watches",
            "Jewelry",
            "Kitchenware",
            "Health & Wellness",
            "Handbags",
            "Automotive",
            "Art & Craft"
        ]
        count_added = 0
        count_already_added = 0
        for name in categories:
            obj, created = Category.objects.get_or_create(name=name)
            if created:
                #print(self.style.SUCCESS(f"Added: {name}"))
                count_added += 1
            else:
                #print(self.style.WARNING(f"Already exists: {name}"))
                count_already_added += 1

        print(self.style.SUCCESS("Categories added successfully!"))
        print(self.style.SUCCESS(f"Added {count_added} new categories"))
        print(self.style.SUCCESS(f"Already added {count_already_added} new categories"))

