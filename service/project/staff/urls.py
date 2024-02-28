from rest_framework.routers import DefaultRouter

from staff.views.staff import StaffView

router = DefaultRouter()
router.register(r'base', StaffView)

urlpatterns = [
]

urlpatterns += router.urls
