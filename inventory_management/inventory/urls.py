
from django.urls import path
from .import views

urlpatterns = [
    path('', views.startup_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('adminLogin/', views.admin_login_view, name='adminLogin'),
    path('admin_dashboard/', views.admin_dashboard_view, name='admin_dashboard'),
    path('add_user/', views.add_user_view, name='add_user'),
    path('remove_user/', views.remove_user_view, name='remove_user'),
    path('inventoryhome/', views.inventoryLogin_view, name='inventoryhome'), 
    # path('exhardForm/', views.xhard_form_view, name='exhardForm'),
    # path('add-product/', views.exhardForm_view, name='add_product'),
    # path('update-product/<int:product_id>/', views.update_exhard, name='update_product'),
  
    path('exhardForm/', views.exhardForm_view, name='exhard_form')
]




