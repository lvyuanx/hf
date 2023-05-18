from rest_framework.routers import DefaultRouter

from order.views.order_base_views import OrderBaseView
from order.views.order_detail_views import OrderDetailView
from order.views.order_list_views import OrderListView
from order.views.order_type_views import OrderTypeView
from order.views.step_base_views import StepBaseView
from order.views.step_sort_views import StepSortView

router = DefaultRouter()
router.register(r'base', OrderBaseView)
router.register(r'list', OrderListView)
router.register(r'type', OrderTypeView)
router.register(r'detail', OrderDetailView)
router.register(r'stepBase', StepBaseView)
router.register(r'stepSort', StepSortView)

urlpatterns = [
]

urlpatterns += router.urls
