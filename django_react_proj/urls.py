from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/students/', views.students_list),
    path('api/students/<pk>', views.students_detail),
]
