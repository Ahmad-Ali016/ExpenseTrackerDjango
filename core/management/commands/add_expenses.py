import random
from logging import exception

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Expense, Category, Tag  # change your_app to your app name
from decimal import Decimal

class Command(BaseCommand):
    help = "Create 40 expenses for user 'knez' with categories and tags"

    def handle(self, *args, **kwargs):
        try:
            user = User.objects.get(username="Ali")
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("❌ User 'Ali' not found!"))
            return

        categories = list(Category.objects.all())
        tags = list(Tag.objects.all())

        if not categories:
            self.stdout.write(self.style.ERROR("❌ No categories found! Add categories first."))
            return

        if not tags:
            self.stdout.write(self.style.ERROR("❌ No tags found! Add tags first."))
            return

        expense_names = [
            "Grocery Shopping", "Fuel Refill", "Lunch at Restaurant", "Monthly Rent",
            "Buying Shoes", "Electricity Bill", "Water Bill", "Haircut", "Online Course",
            "Phone Bill", "Gym Membership", "Netflix Subscription", "New Clothes",
            "Medicine Purchase", "Snacks", "Coffee", "Dinner Delivery", "Car Maintenance",
            "Taxi Ride", "Internet Bill", "School Books", "Movie Tickets",
            "Gift Purchase", "Sports Equipment", "Cleaning Supplies", "Cosmetics",
            "Mobile Accessories", "Laptop Repair", "Travel Booking", "Hotel Payment",
            "Parking Fee", "Toll Tax", "Kids Toys", "Pet Food", "Charity Donation",
            "Kitchen Utensils", "Office Supplies", "Event Tickets", "Insurance Payment"
        ]

        for name in expense_names[:40]:
            category = random.choice(categories)
            amount = Decimal(random.uniform(200, 20000)).quantize(Decimal("0.01"))

            expense = Expense.objects.create(
                user=user,
                category=category,
                name=name,
                amount=amount,
            )

            random_tags = random.sample(tags, random.randint(1, 4))
            expense.tags.set(random_tags)

            self.stdout.write(self.style.SUCCESS(
                f"✔ Created: {expense.name} - {expense.amount}"
            ))

        self.stdout.write(self.style.SUCCESS("\n🎉 Successfully added 40 expenses for user 'knez'!"))
