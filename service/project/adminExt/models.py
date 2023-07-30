from django.db import models

prefix = "s_admin"


class SRole(models.Model):
    users = models.ManyToManyField('auth.User', verbose_name="用户")
    role_name = models.CharField(max_length=100, unique=True, verbose_name="角色名称")
    role_desc = models.CharField(max_length=100, verbose_name="角色描述")
    role_label = models.CharField(max_length=100, verbose_name="角色标识")
    notes = models.TextField(null=True, blank=True, verbose_name="备注")
    is_enable = models.BooleanField(default=True, verbose_name="是否启用")
    create_user = models.BigIntegerField(verbose_name="创建人")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_user = models.BigIntegerField(verbose_name="更新人")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    delete_user = models.BigIntegerField(null=True, blank=True, verbose_name="删除人")
    delete_time = models.DateTimeField(null=True, blank=True, verbose_name="删除时间")

    def __str__(self):
        return self.role_name

    class Meta:
        verbose_name = "角色"
        verbose_name_plural = "角色列表"
        db_table = f"{prefix}_role"


class SPremission(models.Model):
    roles = models.ManyToManyField(SRole, verbose_name="角色")
    permission_name = models.CharField(max_length=100, null=True, blank=True, verbose_name="权限名称")
    permission_desc = models.CharField(max_length=100, null=True, blank=True, verbose_name="权限描述")
    permission_label = models.CharField(max_length=100, null=True, blank=True, verbose_name="权限标识")
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, verbose_name="父级权限")
    menu_icon = models.CharField(max_length=100, null=True, blank=True, verbose_name="图标")
    menu_url = models.CharField(max_length=100, null=True, blank=True, verbose_name="链接")
    notes = models.TextField(null=True, blank=True, verbose_name="备注")
    is_enable = models.BooleanField(default=True, verbose_name="是否启用")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    create_user = models.BigIntegerField(verbose_name="创建人")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_user = models.BigIntegerField(verbose_name="更新人")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    delete_user = models.BigIntegerField(null=True, blank=True, verbose_name="删除人")
    delete_time = models.DateTimeField(null=True, blank=True, verbose_name="删除时间")

    def __str__(self):
        return self.permission_name

    class Meta:
        verbose_name = "权限"
        verbose_name_plural = "权限列表"
        db_table = f"{prefix}_permission"



