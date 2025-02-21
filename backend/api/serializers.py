#whole file is created by me, serialiser convert the api function that we write inside views.py to json form
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

#creating a api to create a new user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"] #these are the data send/receive by the api
        extra_kwargs = {"password":{"write_only": True}} #we want only the password to be send by the frontend not receive so its write_only in the database.
    
    #the above class validates the data send by the user and below function the makes the user
    def create(self, validate_data):
        user = User.objects.create_user(**validate_data) # "**" means all parameters + the validated data (I few know what it means:( )
        return user
 
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author":{"read_only": True}} #we want the author name to be set once by the frontend here
