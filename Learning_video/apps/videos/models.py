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


class Courese(models.Model):

    LEVEL_CHOICES = (
        (1,"初级"),
        (2,"中级"),
        (3,"高级")
        # (1, "python"),
        # (2, "java"),
        # (3, "Linux"),
        # (4,"C/C++"),
        # (5,"PHP"),
        # (6,"大数据"),
        # (7,"go语言"),
        # (8,"web前端"),
        # (9,"Android"),
        # (10,"IOS"),
        # (11,"网络信息")
    )
    courese_name = models.CharField("课程名称",unique=True,max_length=128)
    num = models.IntegerField("课程节数",null=True)
    content = RichTextUploadingField("课程描述",null=True, )
    img = models.ImageField("图片",upload_to="avator/%Y%m%d/", default="avator/default.jpg",)
    tag = models.ForeignKey(Category,verbose_name="标签",null=True,)
    #user = models.ForeignKey(User,verbose_name="观看用户",)
    id = models.IntegerField("编号",primary_key=True)
    class Meta:
        verbose_name = "课程大纲"
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return f"{self.courese_name}"

# class PythonCoures(models.Model):
#     id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
#     coure_name =models.ForeignKey(Courese)
#     data = models.Field(verbose_name="视频")
#     text = models.TextField("全部课程标题",unique=True, max_length=256)
#
#
#     class Meta:
#         managed = False
#         verbose_name = "全部课程"
#         verbose_name_plural = verbose_name
#         ordering = ['id']


class ALLCoureslist(models.Model):
    id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    coure_id =models.ForeignKey(Courese,verbose_name="所有课程",null=True)
    link = models.CharField(verbose_name="视频链接",null=True,max_length=9999)
    text = models.TextField("课程标题",unique=True, max_length=256,null=True)

    class Meta:
        verbose_name = "全部课程视频"
        verbose_name_plural = verbose_name
        ordering = ['id']
#课程目录
# class CouresCatalog(models.Model):
#     name = models.CharField("课程目录",max_length=64)
#
#     class Meta:
#         verbose_name = "目录"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return f"{self.name}"

