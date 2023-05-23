# Generated by Django 4.1.7 on 2023-04-29 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('order', '0002_orderbase_create_time_orderbase_notes_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderbase',
            options={'verbose_name': '订单款号', 'verbose_name_plural': '订单款号列表'},
        ),
        migrations.CreateModel(
            name='OrderList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_technology', models.CharField(max_length=100, null=True, verbose_name='工艺')),
                ('customer', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='customer.customer', verbose_name='客户')),
                ('order_base', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='order.orderbase', verbose_name='款号')),
            ],
            options={
                'verbose_name': '订单列表',
                'verbose_name_plural': '订单列表',
                'db_table': 's_order_list',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='数量')),
                ('color', models.CharField(max_length=100, null=True, verbose_name='颜色')),
                ('order_list', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='order.orderlist', verbose_name='所属订单')),
            ],
            options={
                'verbose_name': '订单项',
                'verbose_name_plural': '订单项',
                'db_table': 's_order_detail',
            },
        ),
    ]