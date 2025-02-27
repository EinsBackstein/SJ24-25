import random
from django.core.management.base import BaseCommand
from faker import Faker
from demoapp.models import Person,Department

# Create 4 departments with the ids 1 to 4

# Define the data
department_data = [
    {'id': 1, 'shortname': 'IT', 'description': 'Informationstechnologie'},
    {'id': 2, 'shortname': 'IF', 'description': 'Informatik'},
    {'id': 3, 'shortname': 'BT', 'description': 'Bautechnik'},
    {'id': 4, 'shortname': 'IH', 'description': 'Innenarchitektur und Holztechnik'},
]

# Create and save the departments
for data in department_data:
    d = Department()
    d.id = data['id']
    d.shortname = data['shortname']
    d.description = data['description']
    d.save()


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
            department_id = random.randint(1,4)  # Associate one of the 4 departments

            # Create and save Person object
            person = Person(
                firstname=firstname,
                lastname=lastname,
                age=age,
                sex=sex,
                description=description,
                department_id=department_id # Little hack to assign the id directly
            )
            person.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {num_records} Person records'))

