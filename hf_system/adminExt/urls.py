from django.urls import path

from adminExt import views

urlpatterns = [
    path("defined/", views.defined, name="defined_view")
]
