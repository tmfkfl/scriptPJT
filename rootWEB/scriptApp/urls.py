from django.urls import path

from scriptApp import views

urlpatterns = [
    path("main/", views.index),

    path("basic/", views.basic),

    path("dom/", views.dom),

    path("ajax/", views.ajax),

    path("maker/", views.maker),

]