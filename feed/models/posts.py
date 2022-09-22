
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone


User = get_user_model()


class Post(models.Model):
    """_summary_
    This model is for any post that a user posts on the website.
    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    description = models.CharField(max_length=255, blank=True)
    pic = models.ImageField(upload_to='media')
    created_at = models.DateTimeField(auto_now_add=True)
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.description
    

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})
