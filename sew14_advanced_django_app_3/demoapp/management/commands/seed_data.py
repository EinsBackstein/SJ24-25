import random
from django.core.management.base import BaseCommand
from faker import Faker
from demoapp.models import Person

class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def add_arguments(self, parser):
        parser.add_argument('num_records', type=int, help='Number of Person records to seed')

    def handle(self, *args, **kwargs):
        # Create an Austrian faker
        f = Faker('de_AT')

        # Clear existing data
        Person.objects.all().delete()

        num_records = kwargs['num_records']

        for _ in range(num_records):
            # Generate random data using Faker
            sex = random.choice(['M', 'F'])
            # Set the first name corresponding to the sex
            firstname = f.first_name_female() if sex == 'F' else f.first_name_male()
            lastname = f.last_name()
            age = random.randint(18, 99)  # Adjust the age range as needed
            description = f.text()

            # Create and save Person object
            person = Person(
                firstname=firstname,
                lastname=lastname,
                age=age,
                sex=sex,
                description=description,
            )
            person.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {num_records} Person records'))

