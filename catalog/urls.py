from django.urls import path
from . import views

urlpatterns = [
    # View (function-based)
    path('', views.index, name='index'),
    #  View (class-based)
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]