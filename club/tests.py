from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm, ResourceForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.meet = Meeting(meetingtitle='test', meetingdate='2021-02-10')

    def test_typestring(self):
        self.assertEqual(str(self.meet),'test' )

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class MinutesTest(TestCase):
    def setUp(self):
        self.meet = Meeting(meetingtitle="test minutes")
        self.minutes = MeetingMinutes(meetingid=self.meet)

    def test_typestring(self):
        self.assertEqual(str(self.minutes), "test minutes" )

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

class ResourceTest(TestCase):
    def setUp(self):
        self.resourcename = Resource(resourcename='test', resourcetype='book')

    def test_typestring(self):
        self.assertEqual(str(self.resourcename),'test' )

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.eventtitle = Event(eventtitle='test', location='Seattle')

    def test_typestring(self):
        self.assertEqual(str(self.eventtitle),'test' )

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class NewMeetingForm(TestCase):
    #valid form data
    def test_meetingform(self):
        data={
                'meetingtitle':'test',
                'meetingdate':'2021-01-01',
                'meetingtime':'11:00am',
                'agenda':'none'
                
        }
        form=MeetingForm (data)
        self.assertTrue(form.is_valid)

class NewResourceForm(TestCase):
    #valid form data
    def test_meetingform(self):
        data={
                'resourcename':'test',
                'resourcetype':'magizine',
                'url':'test.com',
                'dateentered':'2021-05-13',
                'userid':'kevin',
                'description':'none'

                
        }
        form=ResourceForm (data)
        self.assertTrue(form.is_valid)

class New_Meeting_Authentication_Test(TestCase):
    def setUP(self):
        self.test_user = User.objects.create_user(username='testuser1', password='Passw0rd!')
        self.meet = Meeting.objects.create(meetingtitle='test', meetingdate='2021-02-10')
        self.resource = Resource.objects.create(resourcename='test', resourcetype='magizine',url='test.com')

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('newmeeting'))
        self.assertRedirects(response, '/accounts/login/?next=/club/newMeeting/')
