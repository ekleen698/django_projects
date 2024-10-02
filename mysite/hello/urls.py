from django.urls import path

from .views import myview

app_name = "hello"
urlpatterns = [
 path('', myview),
]