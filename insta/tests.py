from django.test import TestCase
from .models import Profile, Image, Comment 
# Create your tests here.

class EventOrganizerTestClass(TestCase):
    
    # Set up method
    def setUp(self):
        self.virsail= EventOrganizer(first_name = 'virsail', last_name ='Mbagaya', email ='virsaileric@gmail.com')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.virsail,EventOrganizer))
    # Testing Save Method
    def test_save_method(self):
        self.virsail.save_eventorganizer()
        eventorganizers = EventOrganizer.objects.all()
        self.assertTrue(len(eventorganizers) > 0)


class EventTestClass(TestCase):
    
    def setUp(self):
        # Creating a new eventorganizer and saving it
        self.virsail= EventOrganizer(first_name = 'Virsail', last_name ='Mbagaya', email ='virsaileric@gmail.com')
        self.virsail.save_eventorganizer()

        # Creating a new ticket and saving it
        self.new_ticket = tickets(name = 'ticketing')
        self.new_ticket.save()

        #self.new_event= Event(title = '',post = '',eventorganizer = self.virsail)
        #self.new_event.save()

        #self.new_event.tickets.add(self.new_ticket)

    def tearDown(self):
        EventOrganizer.objects.all().delete()
        tickets.objects.all().delete()
        Event.objects.all().delete()

    def test_get_event_today(self):
        today_event = Event.todays_event()
        self.assertFalse(len(today_event)>0)
    
    def test_get_event_by_date(self):
        test_date = '2020-10-20'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        event_by_date = Event.days_event(date)
        self.assertTrue(len(event_by_date) == 0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='colorfest254')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

        
    