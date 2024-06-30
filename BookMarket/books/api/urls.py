from django.urls import path
from books.api import views as api_views
urlpatterns = [
    path('books/',api_views.BookListCreateAPIView.as_view(),name="book-list"),
    path('books/<int:pk>',api_views.BookDetailAPIView.as_view(),name="book-detail"),
      
    path('author/',api_views.AuthorListCreateAPIView.as_view(),name="author-list"),
    path('author/<int:pk>',api_views.AuthorDetailAPIView.as_view(),name="author-detail"),
    
     path('books/<int:book_pk>/makecomment/', api_views.CommentCreateAPIView.as_view(), name='make-comment'),
     path('comments/<int:pk>', api_views.CommentDetailAPIView.as_view(), name='comments'),
]
