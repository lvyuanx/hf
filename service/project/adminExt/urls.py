from django.urls import path

from adminExt import admin_view

urlpatterns = [
    path("defined/", admin_view.defined, name="defined_view")
]
