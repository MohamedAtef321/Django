import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_project_1.settings')

import django
django.setup()

## FAKE POP SCRIPT
import random
from dj_app_1.models import AccessRecord, Topic, Webpage, User
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        top = add_topic()

        # create the fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create a fake access record for that webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

def add_user():
    user = User.objects.get_or_create(first_name=fakegen.first_name(),
                                      last_name=fakegen.last_name(),
                                      email=fakegen.email())[0]
    user.save()
    return user

def populate_users(N=5):
    for entry in range(N):
    
        # create the fake data for that entry
        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        user = add_user()

if __name__ == '__main__':
    print("Populating script!")
    populate_users(20)
    print("Populating complete!")

