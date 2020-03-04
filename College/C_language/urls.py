from django.conf.urls import url
from django.urls import include, path
from . import views
app_name = "C_language"
urlpatterns = [

url("^$",views.compile, name='c_compile'),


]