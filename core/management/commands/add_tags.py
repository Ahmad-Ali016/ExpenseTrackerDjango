from django.core.management.base import BaseCommand
from core.models import Tag  # change to your actual app name

class Command(BaseCommand):
    help = "Add 80–100 default tags to the Tag model"

    def handle(self, *args, **kwargs):
        tags = [
            "Food", "Groceries", "Snacks", "Beverages", "Coffee", "Tea",
            "Restaurants", "Fast Food", "Delivery", "Dining Out",
            "Transport", "Fuel", "Taxi", "Uber", "Careem", "Bus", "Train",
            "Car Maintenance", "Parking", "Toll",
            "Shopping", "Clothes", "Shoes", "Accessories", "Cosmetics",
            "Skincare", "Haircare", "Makeup", "Personal Care",
            "Medical", "Pharmacy", "Doctor Visit", "Hospital",
            "Lab Tests", "Vitamins", "Therapy", "Health Insurance",
            "Home", "Rent", "Utilities", "Electricity", "Water", "Gas",
            "Internet", "Mobile Bill", "Cleaning Supplies",
            "Furniture", "Repairs", "Home Improvement",
            "Education", "Tuition", "Books", "Stationery",
            "Online Courses", "Workshops",
            "Entertainment", "Cinema", "Games", "Subscriptions",
            "Netflix", "Amazon Prime", "YouTube", "Spotify",
            "Gym", "Fitness", "Yoga", "Sports", "Cycling",
            "Travel", "Flights", "Hotel", "Tour", "Visa Fees",
            "Luggage", "Travel Insurance",
            "Business", "Office Supplies", "Software", "Hosting",
            "Domain", "Marketing", "Ads", "Client Meeting",
            "Gifts", "Charity", "Donations",
            "Kids", "Babysitting", "Toys", "School Fees",
            "Pets", "Pet Food", "Vet",
            "Miscellaneous", "Emergency", "One-Time Expense",
            "Maintenance", "Bank Fees", "Taxes"
        ]

        for name in tags:
            obj, created = Tag.objects.get_or_create(name=name)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Added: {name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Already exists: {name}"))

        self.stdout.write(self.style.SUCCESS("All tags added successfully!"))
