from django.contrib import admin
from django.utils.html import format_html

from order.models import OrderType, OrderBase, OrderList, StepBase, StepSortChangeRecord, StepSort
from order.utils.utils import sort_steps


@admin.register(OrderType)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', "name")
    list_per_page = 10


@admin.register(OrderBase)
class OrderBaseAdmin(admin.ModelAdmin):
    list_display = ['order_code', 'img_thumbnail', 'order_type', 'order_product', 'create_time', 'notes']
    list_display_links = ('order_code',)
    list_filter = ('order_type', 'create_time')
    search_fields = ('order_code__icontains', 'order_product__icontains')

    def img_thumbnail(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.model_base.model_image.url))

    img_thumbnail.short_description = '模具'

    list_per_page = 10


@admin.register(OrderList)
class OrderListAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_base_link', 'customer', 'order_technology', 'create_time', 'update_time']
    list_display_links = ('order_base_link',)
    search_fields = ('customer__name__icontains', 'customer__contact_number__icontains',
                     'order_base__order_code__icontains')

    def img_thumbnail(self, obj):
        return format_html('<img src="{}" width="50" height="50" />'.format(obj.model_base.model_image.url))

    def order_base_link(self, obj):
        return format_html('<a href="/admin/defined/#/order/list-edit/{}">{}</a>'
                           .format(obj.id, obj.order_base.order_code))

    img_thumbnail.short_description = '模具'
    order_base_link.short_description = '款号'

    list_per_page = 10

    def has_add_permission(self, request):
        return False

    # 增加自定义按钮
    actions = ['custom_button']

    def custom_button(self, request, queryset):
        pass

    # 显示的文本，与django admin一致
    custom_button.short_description = ' 新增'
    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'el-icon-plus'

    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'primary'

    # 链接按钮，设置之后直接访问该链接
    # 3中打开方式
    # action_type 0=当前页内打开，1=新tab打开，2=浏览器tab打开
    # 设置了action_type，不设置url，页面内将报错
    # 设置成链接类型的按钮后，custom_button方法将不会执行。
    custom_button.action_type = 0
    custom_button.action_url = '/admin/defined/#/order/list-edit'


@admin.register(StepBase)
class StepBaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'notes')
    list_display_links = ('name',)

    list_per_page = 10


@admin.register(StepSortChangeRecord)
class StepSortChangeRecordAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_delete=False)

    list_display = ('order_type_link', 'notes', 'step_info_link')
    list_display_links = ('order_type_link',)
    list_per_page = 10

    def order_type_link(self, obj):
        return format_html('<a href="/admin/defined/#/order/step-edit/{}">{}</a>'
                           .format(obj.id, obj.order_type))

    def step_info_link(self, obj):
        # 查询order_type对应的所有步骤
        step_sort_lst = StepSort.objects.filter(change_record_id=obj.id)

        # 根据parent_step和child_step的关系，生成链表
        step_sort_lst = sort_steps(list(step_sort_lst))
        info_lst = []
        for step in step_sort_lst:
            is_skip = step.step_base.is_skip
            span_color = '#f4f4f5' if is_skip else '#409eff'
            font_color = '#a2a5aa' if is_skip else '#fff'
            info_lst.append('<span href="" '
                            'style="background-color: {};'
                            'padding: 3px;color:{};'
                            'border-radius: 3px;'
                            'white-space: nowrap;">{}</span>'
                            .format(span_color, font_color, step.step_base.name))
        step_info = ' -> '.join(info_lst)
        return format_html(step_info)

    step_info_link.short_description = '流程'
    order_type_link.short_description = '订单类型'

    def has_add_permission(self, request):
        return False

    # 增加自定义按钮
    actions = ['custom_button']

    def custom_button(self, request, queryset):
        pass

    # 显示的文本，与django admin一致
    custom_button.short_description = ' 新增'
    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'el-icon-plus'

    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'primary'

    # 链接按钮，设置之后直接访问该链接
    # 3中打开方式
    # action_type 0=当前页内打开，1=新tab打开，2=浏览器tab打开
    # 设置了action_type，不设置url，页面内将报错
    # 设置成链接类型的按钮后，custom_button方法将不会执行。
    custom_button.action_type = 0
    custom_button.action_url = '/admin/defined/#/order/step-edit'


# @admin.register(StepSort)
# class StepSortAdmin(admin.ModelAdmin):
#
#     def get_queryset(self, request):
#         return super().get_queryset(request).filter(parent_step__isnull=True)
#
#     list_display = ('order_type', 'step_base', 'step_info_link')
#     list_display_links = ('order_type',)
#
#     list_per_page = 10
#
#     @staticmethod
#     def sort_step(step_lst):
#         """根据parent_step和child_step的关系，生成链表"""
#         step_sort_lst = []
#
#         # 找到头节点
#         first_step = None
#         step_idx = -1
#         for idx, step in enumerate(step_lst):
#             if step.parent_step is None:
#                 first_step = step
#                 step_idx = idx
#                 break
#
#         if step_idx == -1:
#             return step_sort_lst
#
#         # 删除找到的头节点
#         del step_lst[step_idx]
#
#         # 生成链表
#         step_sort_lst.append(first_step)
#
#         while len(step_lst) > 0:
#             sort_last_step = step_sort_lst[-1]
#             for idx, step in enumerate(step_lst):
#                 if step.parent_step == sort_last_step:
#                     step_sort_lst.append(step)
#                     del step_lst[idx]
#                     break
#
#         return step_sort_lst
#
#     def step_info_link(self, obj):
#         step_info = ''
#         # 查询order_type对应的所有步骤
#         step_list = StepSort.objects.filter(order_type=obj.order_type)
#         # 根据parent_step和child_step的关系，生成链表
#         step_sort_lst = self.sort_step(list(step_list))
#         info_lst = []
#         for step in step_sort_lst:
#             is_skip = step.is_skip
#             span_color = '#f4f4f5' if is_skip else '#409eff'
#             font_color = '#a2a5aa' if is_skip else '#fff'
#             info_lst.append('<span href="" '
#                             'style="background-color: {};'
#                             'padding: 3px;color:{};'
#                             'border-radius: 3px;'
#                             'white-space: nowrap;">{}</span>'
#                             .format(span_color, font_color, step.step_base.name))
#         step_info = ' -> '.join(info_lst)
#         return format_html(step_info)
#
#     step_info_link.short_description = '步骤信息'


admin.site.site_header = '鸿富后台管理系统'  # 设置header
admin.site.site_title = '鸿富后台管理系统'  # 设置title
admin.site.index_title = '鸿富后台管理系统'
