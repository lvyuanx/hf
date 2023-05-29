import os

from django.db import models

from customer.utils import get_upload_path

prefix = "s_customer"


class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="客户名称")
    company_name = models.CharField(max_length=100, unique=True, verbose_name="公司名称")
    contact_number = models.CharField(max_length=20, unique=True, verbose_name="联系电话")
    avatar = models.ImageField(upload_to=get_upload_path, verbose_name="头像")
    notes = models.TextField(blank=True, verbose_name="备注")

    def __str__(self):
        return f"{self.name}-{self.contact_number}"

    class Meta:
        verbose_name = "客户"
        verbose_name_plural = "客户列表"
        db_table = f"{prefix}_base"
