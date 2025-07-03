from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Notes(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile_pics/",default="profile_pics/default.jpeg")

    def __str__(self):
        return f"{self.user.username} Profile"

