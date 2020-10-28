from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField


# Create your models here.

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile_photo= models.ImageField(upload_to='savage/',null=True)
    bio= models.CharField(max_length=230, null=True)


    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def find_profile(cls,search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile

class Image(models.Model):
    posted_by = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    insta_image = models.ImageField(upload_to='mode/',null=True)
    caption = models.TextField(null=True)
    likes = models.PositiveIntegerField(default=0)
    #comments = models.TextField(null=True)


    @classmethod
    def get_images(cls):
        images = Image.objects.all()
        return images

    def __str__(self):
       return str(self.caption)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

class Follow(models.Model):
    users=models.ManyToManyField(User,related_name='follow')
    current_user=models.ForeignKey(User,related_name='pd_user',null=True)

    @classmethod
    def follow(cls,current_user,new):
        friends,created=cls.objects.get_or_create(current_user=current_user)
        friends.users.add(new)

    @classmethod
    def unfollow(cls,current_user,new):
        friends,created=cls.objects.get_or_create(current_user=current_user)
        friends.users.remove(new)

class Comment(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments',null=True)
    comment = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.comment



    @classmethod
    def get_comment(cls):
        comment = Comment.objects.all()
        return comment



    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()