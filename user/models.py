from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    img = models.ImageField(default='default.png', upload_to="blog-pics")

    def __str__(self):
        return f'{self.user.username} profile'