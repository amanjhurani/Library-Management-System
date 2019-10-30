from .views import *
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index ,name='index'),
    path('books/', BookList.as_view() ,name='home'),
    path('book-add/', BookAddView.as_view() ,name='book_add'),
    path('book-issue/<int:pk>/', BookIssueView.as_view() ,name='book_issue'),
    path('search/',views.search)
]
