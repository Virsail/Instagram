from django.test import TestCase
from .models import Profile, Image, Comment 
from django.contrib.auth.models import User
# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='Virsail')
        self.user.save()

        self.profile_test = Profile(id=1, bio='reach out whenever you feel like things rea getting out of hand',user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
       #self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)


class TestImage(TestCase):
    def setUp(self):
        self.profile_test = Profile()
        self.profile_test.save()

        self.image_test = Image(caption='The guy just thought we are stupid', profile=self.profile_test)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    

class TestComment(TestCase):
    def setUp(self):
       #self.profile_test = Profile(name='virsail')
       #self.profile_test.save()

        self.comment_test = Comment(comment='I like this shit')

    def test_instance(self):
        self.assertTrue(isinstance(self.comment_test, Comment))

    def test_save_comment(self):
        self.comment_test.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_comment(self):
       #self.comment_test.delete_comment()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)
        
    