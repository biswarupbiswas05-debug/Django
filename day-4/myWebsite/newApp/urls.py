
from django.contrib import admin
from django.urls import path
from newApp import views   # ✅ IMPORTANT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.app, name='app'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('product/<int:id>/', views.product_details, name='product_details'),

]
