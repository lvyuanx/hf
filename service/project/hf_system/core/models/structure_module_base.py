from django.db import models


class StructureModuleBase(object):
    is_enable = models.BooleanField(default=True, verbose_name="是否启用")
    create_user = models.BigIntegerField(verbose_name="创建人")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_user = models.BigIntegerField(verbose_name="更新人")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    delete_user = models.BigIntegerField(null=True, blank=True, verbose_name="删除人")
    delete_time = models.DateTimeField(null=True, blank=True, verbose_name="删除时间")
