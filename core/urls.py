from django.urls import path
from core.views import testing_view, health_check, TransactionListView, TransactionDetailView, BudgetListView

urlpatterns = [
    path('testing/', testing_view, name='testing'),
    path('health', health_check, name='health'),
    path('transactions/', TransactionListView.as_view(), name='transaction-list'),
    path('transactions/<int:id>/', TransactionDetailView.as_view(), name='transaction-detail'),
    path('budgets/', BudgetListView.as_view(), name='budget-list'),
]