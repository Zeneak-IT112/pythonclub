from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event

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