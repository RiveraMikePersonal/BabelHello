from django.urls import path
from hello import views

urlpatterns = [
    path("", views.home, name="home"),
    path("hello/",views.babel, name="babel" ),
    path("hello/translate",views.translate, name="translate" )
]