from django.db import models
from django.contrib.auth import get_user_model
from . import Post


User = get_user_model()


class Comments(models.Model):
    """_summary_
    Comment model links a comment with the post and the user
    Args:
        models (_type_): _description_
    """
    post = models.ForeignKey("Post",related_name="details",on_delete=models.CASCADE)
    username = models.ForeignKey(User,related_name='details',on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    comment_date = models.DateTimeField(auto_now_add=True)
    
