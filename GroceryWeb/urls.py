from django.urls import path
from General import views

urlpatterns = [
    path('api/dashboard/', views.dashboard_api),
    path('api/contacts/', views.contact_mgmt_api),
    path('api/contacts/delete/<int:id>/', views.delete_contact_api),
    path('api/orders/', views.order_mgmt_api),
    path('api/products/', views.product_mgmt_api),
    path('api/products/add/', views.add_product_api),
    path('api/logout/', views.admin_logout_api),
    path('api/register/', views.register_api),
    path('api/login/', views.login_api),
]
