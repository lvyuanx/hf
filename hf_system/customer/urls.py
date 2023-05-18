from rest_framework.routers import DefaultRouter

from customer.views.customer_views import CustomerView

router = DefaultRouter()
router.register(r'customer', CustomerView)


urlpatterns = [
]

urlpatterns += router.urls
