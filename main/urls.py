from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index,name="index"),
    path("", views.home,name="home"),
    path("create/",views.create,name="create"), 
    path("practice/",views.practice,name="practice"),
    path("excelfile/",views.upload_file,name="uploadfile"),
]