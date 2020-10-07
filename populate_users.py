import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Bank_system.settings")

import django
django.setup()

from Users.models import Users
from faker import Faker

fakegen = Faker()

def populate(N):
    for entry in range(N):
        fake_profile = fakegen.simple_profile()
        fake_name = fake_profile['name']
        fake_email = fake_profile['mail']
        fake_gender = fake_profile['sex']
        fake_address = fake_profile['address']
        fake_date_of_birth = str(fake_profile['birthdate'])
        fake_balance = fakegen.random_int(1000,100000)

        user = Users.objects.get_or_create(name=fake_name, email=fake_email, gender=fake_gender, address=fake_address,
                                            date_of_birth=fake_date_of_birth, balance=fake_balance)[0]

if __name__ == '__main__':
    print("Populating Databases!")
    populate(10)
    print("Complete!")