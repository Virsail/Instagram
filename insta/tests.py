from django.test import TestCase
from .models import Profile, Image, Comment 
from django.contrib.auth.models import User
# Create your tests here.

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='Virsail')
        self.user.save()

        self.profile_test = Profile(id=1, name='mode', profile_picture='grid.png', bio='reach out whenever you feel like things rea getting out of hand',
                                    user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))

    def test_save_profile(self):
        self.profile_test.save_profile()
        after = Profile.objects.all()
        self.assertTrue(len(after) > 0)


class TestImage(TestCase):
    def setUp(self):
        self.profile_test = Profile(name='virsail')
        self.profile_test.save()

        self.image_test = Image(image='grid.png', name='savage', caption='The guy just thought we are stupid', user=self.profile_test)

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, Image))

    def test_save_image(self):
        self.image_test.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)

class TestComment(TestCase):
    def setUp(self):
        self.profile_test = Profile(name='virsail')
        self.profile_test.save()

        self.comment_test = Comment(image='grid.png', poster='virsail', comment='I like this shit')

        def test_instance(self):
        self.assertTrue(isinstance(self.comment_test, Comment))

    def test_save_comment(self):
        self.comment_test.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_comment(self):
        self.comment_test.delete_comment()
        after = Profile.objects.all()
        self.assertTrue(len(after) < 1)
        
    