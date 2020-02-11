from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
from .vaild_difficulty import valid_difficulty,valid_difficulty1
from ckeditor_uploader.fields import RichTextUploadingField
from apps.user.models import User
class Category(models.Model):
    """分类"""
    name = models.CharField("分类名称", max_length=64)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.name}"
tag_choices = (
        (1, "python"),
        (2, "java"),
        (3, "Linux"),
        (4,"C/C++"),
        (5,"PHP"),
        (6,"大数据"),
        (7,"go语言"),
        (8,"web前端"),
        (9,"Android"),
        (10,"IOS"),
        (11,"网络信息")
    )
class Tag(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='id')
    tag = models.CharField(max_length=20,verbose_name='标签名',choices=tag_choices)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.tag}"

class Courese(models.Model):

    LEVEL_CHOICES = (
        (1, "python"),
        (2, "java"),
        (3, "Linux"),
        (4,"C/C++"),
        (5,"PHP"),
        (6,"大数据"),
        (7,"go语言"),
        (8,"web前端"),
        (9,"Android"),
        (10,"IOS"),
        (11,"网络信息")
    )
    courese_name = models.CharField("课程名称",max_length=128,unique=True)
    num = models.IntegerField("课程节数",null=True)
    content = RichTextUploadingField("课程描述",null=True, )
    img = models.ImageField("图片",upload_to="avator/%Y%m%d/", default="avator/default.jpg",)
    tag = models.ForeignKey(Tag,verbose_name="标签",null=True,)
    #user = models.ForeignKey(User,verbose_name="观看用户",)
    id = models.AutoField("编号",primary_key=True)
    view_count = models.IntegerField(default=0,blank=True)
    # liked = models.ManyToManyField(User,blank=True,verbose_name="喜欢的视频",related_name='liked_videos')
    collected = models.ManyToManyField(User,blank=True,verbose_name="收藏",related_name='collected_videos')
    create_time = models.DateTimeField(blank=True,max_length=20,default='2019-7-7',null=True)

    def increase_view_count(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])

    class Meta:
        verbose_name = "课程大纲"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return f"{self.courese_name}"


    def switch_collect(self, user):
        if user in self.collected.all():
            self.collected.remove(user)
            self.save()

        else:
            self.collected.add(user)
            self.save()

    def user_collected(self,user):
        if user in self.collected.all():
            return 1
        else:
            return 0

class ALLCoureslist(models.Model):
    id = models.AutoField(verbose_name='视频编号',primary_key=True,unique=True)  # Field name made lowercase.
    coure_id =models.ForeignKey(Courese,verbose_name="课程编号",null=True)
    link = models.CharField(verbose_name="视频链接",null=True,max_length=999999)
    title = models.CharField(verbose_name="课程标题", max_length=256,null=True)
    class Meta:
        verbose_name = "全部课程视频"
        verbose_name_plural = verbose_name
        ordering = ['id']

