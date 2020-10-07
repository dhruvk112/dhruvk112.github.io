from django.urls import path
from Users import views

app_name = 'users'

urlpatterns = [
    path('',views.UserListView.as_view(),name="list"),
    path('transactions/',views.TransactionListView.as_view(),name="transaction"),
    path('<int:pk>/',views.UserDetailView.as_view(),name='detail'),
    path('transfer/<int:pk>/',views.UserTransferView.as_view(),name='transfer'),
]