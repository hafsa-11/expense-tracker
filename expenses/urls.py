from django.urls import path
from .views import index, delete_expense, edit_expense

urlpatterns = [
    path('', index, name='index'),
    path('delete/<int:expense_id>/', delete_expense, name='delete_expense'),
    path('edit/<int:expense_id>/', edit_expense, name='edit_expense'),
]
