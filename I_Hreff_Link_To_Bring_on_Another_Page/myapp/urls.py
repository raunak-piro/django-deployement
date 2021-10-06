from django.contrib import admin
from django.urls import path
from myapp import views
app_name='myapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index,name='index'),
    path('other',views.other,name='other'),
]
