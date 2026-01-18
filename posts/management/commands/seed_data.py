from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from posts.models import Post, Comment
from faker import Faker
import random

# Get the correct User model (works even if it's in a different app)
User = get_user_model()


class Command(BaseCommand):
    help = "Seeds the database with dummy data"

    def handle(self, *args, **kwargs):
        fake = Faker()

        self.stdout.write(self.style.SUCCESS("Creating Users..."))
        users = []

        # 1. Create a Demo User (For logging in)
        demo_email = "test@test.com"

        try:
            # Check if the demo user already exists
            if not User.objects.filter(email=demo_email).exists():
                demo_user = User.objects.create_user(
                    username="test", email=demo_email, password="noufal"
                )
                users.append(demo_user)
                self.stdout.write(f"Created Demo User: {demo_email}")
            else:
                # If exists, add to the list
                users.append(User.objects.get(email=demo_email))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error creating demo user: {e}"))

        # 2. Create 10 random users
        for _ in range(10):
            try:
                user = User.objects.create_user(
                    username=fake.unique.user_name(),
                    email=fake.unique.email(),
                    password="noufal",
                )
                users.append(user)
            except:
                continue  # Skip if any error occurs (e.g., duplicate data)

        self.stdout.write(self.style.SUCCESS("Creating Posts..."))

        # 3. Create 50 posts (Ensure we have users first)
        if users:
            for _ in range(50):
                created_post = Post.objects.create(
                    author=random.choice(users),  # Select a random author
                    title=fake.sentence(),
                    content=fake.paragraph(nb_sentences=10),
                )
                Comment.objects.create(
                    author=random.choice(users),  # Select a random author
                    content=fake.paragraph(nb_sentences=10),
                    post=created_post,
                )
            self.stdout.write(self.style.SUCCESS("Successfully seeded data! 🚀"))
            self.stdout.write(
                self.style.WARNING(
                    f"Login with -> Email: {demo_email} | Password: noufal"
                )
            )
        else:
            self.stdout.write(
                self.style.ERROR("No users created, cannot create posts!")
            )
