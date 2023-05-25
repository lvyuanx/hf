from django.db import models

from customer.models import Customer
from factory.models import ModelInfo

prefix = "s_order"


class OrderType(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name="订单类型")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "订单类型"
        verbose_name_plural = "订单类型管理"
        db_table = f'{prefix}_type'


class OrderBase(models.Model):
    order_code = models.CharField(max_length=100, verbose_name="款号")
    order_type = models.ForeignKey(OrderType, on_delete=models.CASCADE, db_constraint=False, verbose_name="订单类型")
    model_base = models.ForeignKey(ModelInfo, on_delete=models.CASCADE, db_constraint=False, verbose_name="模具名称")
    order_product = models.CharField(max_length=100, null=True, verbose_name="产品名称")
    notes = models.TextField(blank=True, verbose_name="备注")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return self.order_code

    class Meta:
        verbose_name = "订单款号"
        verbose_name_plural = "订单款号列表"
        db_table = f"{prefix}_base"


class OrderList(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_constraint=False, verbose_name="客户")
    order_base = models.ForeignKey(OrderBase, on_delete=models.CASCADE, db_constraint=False, verbose_name="款号")
    order_technology = models.CharField(max_length=100, null=True, verbose_name="工艺")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    def __str__(self):
        return f'{self.customer.name}-{self.order_base.order_code}'

    class Meta:
        verbose_name = "订单列表"
        verbose_name_plural = "订单列表"
        db_table = f"{prefix}_list"


class OrderDetail(models.Model):
    order_number = models.IntegerField(verbose_name="数量")
    order_price = models.FloatField(verbose_name="单价", default=0.0)
    color = models.CharField(max_length=100, null=True, verbose_name="颜色")
    order_list = models.ForeignKey(OrderList, on_delete=models.CASCADE, db_constraint=False, verbose_name="所属订单")
    notes = models.TextField(blank=True, verbose_name="备注")

    def __str__(self):
        return f'{self.order_list.order_base.order_code}-{self.color}'

    class Meta:
        verbose_name = "订单项"
        verbose_name_plural = "订单项"
        db_table = f"{prefix}_detail"


class StepBase(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="步骤名称")
    notes = models.TextField(blank=True, verbose_name="备注")
    is_skip = models.BooleanField(default=False, verbose_name="是否跳过")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "步骤"
        verbose_name_plural = "步骤列表"
        db_table = f"{prefix}_step_base"


class StepSortChangeRecord(models.Model):
    order_type = models.ForeignKey(OrderType, on_delete=models.CASCADE, db_constraint=False, verbose_name="订单类型")
    notes = models.TextField(blank=True, verbose_name="备注")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")

    class Meta:
        verbose_name = "步骤排序变更记录"
        verbose_name_plural = "步骤排序变更记录"
        db_table = f"{prefix}_step_sort_change_record"


class StepSort(models.Model):
    step_base = models.ForeignKey(StepBase, on_delete=models.CASCADE, db_constraint=False, verbose_name="步骤")
    change_record = models.ForeignKey(StepSortChangeRecord, on_delete=models.CASCADE, db_constraint=False,
                                      verbose_name="变更记录")
    parent_step_id = models.BigIntegerField(null=True, blank=True, verbose_name="父步骤")
    child_step_id = models.BigIntegerField(null=True, blank=True, verbose_name="子步骤")
    is_skip = models.BooleanField(default=True, verbose_name="是否跳过")

    def __str__(self):
        return f'{self.order_type.name}-{self.step_base.name}'

    class Meta:
        verbose_name = "步骤排序"
        verbose_name_plural = "步骤排序"
        db_table = f"{prefix}_step_sort"


class StepRecord(models.Model):
    order_list = models.ForeignKey(OrderList, on_delete=models.CASCADE, db_constraint=False, verbose_name="所属订单")
    step_sort = models.ForeignKey(StepSort, on_delete=models.CASCADE, db_constraint=False, verbose_name="步骤排序")
    start_time = models.DateTimeField(null=True, blank=True, verbose_name="开始时间")
    end_time = models.DateTimeField(null=True, blank=True, verbose_name="结束时间")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    notes = models.TextField(blank=True, verbose_name="备注")

    def __str__(self):
        return f'{self.order_list.order_base.order_code}-{self.step_base.name}'

    class Meta:
        verbose_name = "步骤记录"
        verbose_name_plural = "步骤记录"
        db_table = f"{prefix}_step_record"
