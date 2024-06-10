from django.urls import path
from . import views


urlpatterns = [
    path('books', views.BooksCreateListView.as_view()),
    path('books/<str:bookID>', views.BookDetailVieworDeleteBookView.as_view()),
]