from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.



class Post(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    text = models.CharField(max_length=500)
    image = models.ImageField(upload_to="media/",blank=True,null=True)
    

    def __str__(self):
        return f"{self.name}: {self.text}"
    

class Comment(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    comment = models.CharField(max_length=250)
    post = models.ForeignKey(Post,on_delete=models.SET_NULL, null=True,related_name="message")

    def __str__(self):
        return f"{self.name}: {self.comment}" 
