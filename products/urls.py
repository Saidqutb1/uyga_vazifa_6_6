from django.urls import path
from .views import *

app_name = 'products'
urlpatterns = [
    path('test/', ListView.as_view(), name='book-list'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='book_detail')
]



