from django.db import models
from django.contrib.auth import get_user_model
from . import Post

User = get_user_model()


class Like(models.Model):
    """_summary_
    It stores the like information.
    and it has the user who created the like and the post on which like was made.
    Args:
        models (_type_): _description_
    """
    user = models.ForeignKey(
        User, related_name="likes", on_delete=models.CASCADE)
    post = models.ForeignKey(
        "Post", related_name="likes", on_delete=models.CASCADE)
