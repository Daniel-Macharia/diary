from rest_framework import serializers

from userAuth.models import User
from memory.models import Event as Memory, Day

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userID', 'userName', 'userEmail', 'userPassword')
    

class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Memory
        fields = ( "date", "eventID", "eventTitle", "eventDescription")
    

