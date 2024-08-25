from django.core.management import BaseCommand
from django.contrib.auth.models import User
from main.models import Folder , Html
from os import system
from config.settings import DATABASES
from django.contrib.auth.models import User

class Command(BaseCommand):
    
    # to create superuser on debug run tihis command 
    # $ python manage.py cs
    # beter way to create superuser on debug

    
    def handle(self, *args , **options):
        system("clear")
        # step 1
        db_path = DATABASES["default"]["NAME"]
        system(f"rm -rf {db_path}")
        system("python manage.py makemigrations")
        system("python manage.py migrate")
        user = User.objects.create_superuser(username="reza" , email="reza@gmail.com" , password="reza1313" )
        user.save()


        system("python manage.py runserver")