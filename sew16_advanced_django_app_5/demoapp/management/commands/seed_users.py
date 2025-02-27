# Import the needed models
from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand
from faker import Faker
import random

# Create the faker object
f = Faker('de_AT')

# Use the same default password for all users
default_password = 'defaultPassword123'

# Get the two groups and add them to the groups list
admins_group = Group.objects.get(name='Admins')
managers_group = Group.objects.get(name='Managers')
groups = [admins_group, managers_group]


class Command(BaseCommand):#
    
    def add_arguments(self, parser):
        parser.add_argument('num_records', type=int, help='Number of Person records to seed')

    def handle(self, *args, **kwargs):
        # Create an Austrian faker
        f = Faker('de_AT')


        num_records = kwargs['num_records']

        for _ in range(num_records):
            # Set the user data
            username = f.user_name()
            email = f.email()

            # Create the user object
            user = User(username = username, email = email)

            # Use the set_password() method that hashes the password
            user.set_password(default_password)

            # Save the user before you add the group
            user.save()

            # Add the user to one of the two groups in the list
            user.groups.add(random.choice(groups))

