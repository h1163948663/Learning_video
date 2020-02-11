from django.db import models
from apps.user.models import User
from apps.videos.models import ALLCoureslist
# Create your models here.
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=30,blank=True, null=True)
    avatar = models.CharField(max_length=100,blank=True, null=True)
    video = models.ForeignKey(ALLCoureslist, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "v_comment"