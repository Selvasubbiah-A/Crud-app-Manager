from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('crud/', views.crud_view, name='crud-page'),
    path('crud/add_employee/', views.add_employee, name='add_employee'),
    path('crud/view_employees/', views.view_employees, name='view_employees'),
    path('crud/edit_employees/<int:employee_id>/', views.edit_employee, name='edit_employees'),
    path('crud/view_employees/delete_employee/<int:id>/', views.delete_employee, name='delete_employee'),
]
