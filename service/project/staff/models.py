import os
import uuid

from django.db import models

prefix = "s_staff"


def staff(instance, filename, img_type='avatar'):
    return os.path.join(img_type, str(instance.id), f'{uuid.uuid4()}_{filename}')


class StaffBase(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, db_constraint=False, verbose_name="用户")
    staff_code = models.CharField(max_length=100, unique=True, verbose_name="员工编号")
    phone_number = models.CharField(max_length=100, verbose_name="手机号")
    avatar = models.ImageField(upload_to=staff, null=True, blank=True, verbose_name="头像")
    notes = models.TextField(blank=True, verbose_name="备注")

    def __str__(self):
        return self.staff_code

    class Meta:
        verbose_name = "员工"
        verbose_name_plural = "员工列表"
        db_table = f"{prefix}_base"
