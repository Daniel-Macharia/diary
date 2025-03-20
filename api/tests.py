from django.test import TestCase

from userAuth.models import User
from memory.models import Event as Memory, Day

# Create your tests here.
class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(userID=1, userName="users name", userProfilePicture='profile_pic_url', userEmail='user@example.com', userPassword='userPassword')
    
    def test_user_id(self):
        user = User.objects.get(userID=1)
        expected_user_id = 1

        self.assertEqual(user.userID, expected_user_id)

    def test_user_name(self):
        user = User.objects.get(userID=1)
        expected_user_name = 'users name'

        self.assertEqual(user.userName, expected_user_name)
    
    def test_user_email(self):
        user = User.objects.get(userID=1)
        expected_user_email = 'user@example.com'

        self.assertEqual(user.userEmail, expected_user_email)
    
    def test_user_id(self):
        user = User.objects.get(userID=1)
        expected_user_password = 'userPassword'

        self.assertEqual(user.userPassword, expected_user_password)
    


#test memory classes
class MemoryModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create(userID=23, userName="users name", userProfilePicture='profile_pic_url', userEmail='user@example.com', userPassword='userPassword')
        day = Day.objects.create(userID=user, date="2025-12-28", title="new day")
        Memory.objects.create(date=day, eventID=1, eventTitle="new event", eventDescription="description")
    
    def test_date(self):
        memory_day = Memory.objects.get(eventID=1).date
        expected_date = "2025-12-28"

        self.assertEqual(memory_day.date, expected_date)
    
    def test_eventID(self):
        memory = Memory.objects.get(eventID=1)
        expected_event_id = 1
        
        self.assertEqual(memory.eventID, expected_event_id)

    
    def test_eventTitle(self):
        memory = Memory.objects.get(eventID=1)
        expected_event_title = "new event"
        
        self.assertEqual(memory.eventTitle, expected_event_title)
    
    def test_date(self):
        memory = Memory.objects.get(eventID=1)
        expected_event_description = "description"
        
        self.assertEqual(memory.eventDescription, expected_event_description)
    
