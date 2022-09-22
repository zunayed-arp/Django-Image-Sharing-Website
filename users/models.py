from email.policy import default
from operator import imod
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db.models.signals import post_save
from django.conf import settings


User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default="default.png",upload_to="profile_pics")
    slug = models.SlugField(unique=True,unique_for_date=True)
    bio=models.CharField(max_length=255,blank=True)
    friends = models.ManyToManyField("Profile",blank=True)
    
    def __str__(self) -> str:
        return self.user.username
    
    def get_absolute_url(self):
        return  f"/users/{self.slug}"
    
def post_save_user_model_receiver(sender,instance,created,*args,**kwargs):
    if created:
        try:
            Profile.objects.create(user=instance)
        except:
            pass
post_save.connect(post_save_user_model_receiver,sender=settings.AUTH_USER_MODEL)


class FriendRequest(models.Model):
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user',on_delete=models.CASCADE)
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='from_user',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f"From {self.from_user.username} to {self.to_user.username}"
    
    

