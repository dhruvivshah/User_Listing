#fetches the data from randomuser.me
import requests
from django.core.management.base import BaseCommand
from users.models import User

class Command(BaseCommand):
    help = 'Fetch users from Random User API'

    def handle(self, *args, **kwargs):            
        print("Fetching users...")
        #num_results = 50           inorder to view more number of users
        response = requests.get('https://randomuser.me/api/?results=10')  #can fetch 10 random users from randomuser.me
        print("Response status code:", response.status_code)
        if response.status_code == 200:
            data = response.json()    #converting data to json format
            for user_data in data['results']:
                user = User(
                    name=user_data['name']['first'] + ' ' + user_data['name']['last'],   #concatenate the string
                    gender=user_data['gender'],
                    email=user_data['email'],
                    phone=user_data['phone'],
                    address=str(user_data['location']['street']['number']) + ' ' + user_data['location']['street']['name']  # Convert number to string
                )
                user.save()
            self.stdout.write(self.style.SUCCESS('Successfully fetched and saved users'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch users: ' + str(response.status_code)))