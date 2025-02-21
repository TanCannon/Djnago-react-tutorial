from django.shortcuts import render

#added by me#
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.
#the below class is a built in to handel creating a view for creating user#
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all() #we look at all the Users to make sure we don't duplicate
    serializer_class = UserSerializer #this specifies what kind of User should we accept (the parameters,  fields = ["id", "username", "password"]    )
    permission_classes = [AllowAny] #allow anyone to create a user

class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author = self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)