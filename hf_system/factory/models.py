from django.db import models

from factory.utils import get_upload_path

prefix = "s_factory"


class ModelInfo(models.Model):
    model_image = models.ImageField(upload_to=get_upload_path, null=True, verbose_name="模具图片")
    name = models.CharField(max_length=32, unique=True, verbose_name="名称")
    goods_shelf = models.CharField(max_length=32, null=True, verbose_name="货架")
    row = models.CharField(max_length=32, null=True, verbose_name="行")
    col = models.CharField(max_length=32, null=True, verbose_name="列")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "模具"
        verbose_name_plural = "模具列表"
        db_table = "s_factory_model_base"

