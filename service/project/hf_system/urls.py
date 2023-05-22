from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from adminExt import urls as admin_ext_urls
from order import urls as order_urls
from customer import urls as customer_urls

urlpatterns = [
                  path("admin/", include(admin_ext_urls)),
                  path('admin/', admin.site.urls),
                  path('order/', include(order_urls)),
                  path('customer/', include(customer_urls))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
