from rest_framework.routers import DefaultRouter

from .views.s_role import SRoleView

router = DefaultRouter()
router.register(r'role', SRoleView)

urlpatterns = [
]

urlpatterns += router.urls
