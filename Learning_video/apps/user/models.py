
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from Learning_video.settings import MEDIA_ROOT
from libs.images import make_thumb
from django.db.models.fields.files import ImageFieldFile
import os

class User(AbstractUser):
    id  = models.AutoField(primary_key=True,verbose_name="id")
    realname = models.CharField(max_length=8, verbose_name="真实姓名")
    mobile = models.CharField(max_length=11, verbose_name="手机号")
    qq = models.CharField(max_length=10, verbose_name="QQ号")
    avator_sor = models.ImageField(upload_to="avator/%Y%m%d/", default="avator/default.jpg", verbose_name="头像")
    # avator_sm = models.ImageField("头像缩略图", upload_to="avator/%Y%m%d/", default='avator/default.70x70.jpg')

    # def save(self, *args, **kwargs):
    #     # 将上传的图片先保存
    #     super().save()
    #     # 　如果是默认图片不压缩
    #     if self.avator_sor.name == 'avator/default.jpg':
    #         return
    #     # 如果文件不存在，不压缩
    #     if not os.path.exists(os.path.join(MEDIA_ROOT, self.avator_sor.name)):
    #         return
    #
    #     base, ext = os.path.splitext(self.avator_sor.name)
    #     # 从头像中生成缩略图
    #     thumb_pixbuf = make_thumb(os.path.join(MEDIA_ROOT, self.avator_sor.name), size=THUMB_SIZE)
    #
    #     if thumb_pixbuf:
    #         # 缩略图的保存文件全路径=> 保存文件
    #         thumb_path = os.path.join(MEDIA_ROOT, base + f'.{THUMB_SIZE}x{THUMB_SIZE}' + ext)
    #         # 缩略图相对路径 => 数据库(以下两种取相对路径都可)
    #         relate_thumb_path = os.path.join('/'.join(self.avator_sor.name.split('/')[:-1]),
    #                                          os.path.basename(thumb_path))
    #         relate_thumb_path = base + f'.{THUMB_SIZE}x{THUMB_SIZE}' + ext
    #         # 保存缩略图
    #         thumb_pixbuf.save(thumb_path)
    #         # 保存字段值
    #         self.avator_sm = ImageFieldFile(self, self.avator_sm, relate_thumb_path)
    #     super().save()  # 再保存一下，包括缩略图等