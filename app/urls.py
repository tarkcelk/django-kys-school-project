from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('library', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('add_book', views.add_book, name='add_book'),
    path('add_member', views.add_member, name='add_member'),
    path('members', views.members, name='members'),
    path('barrow_a_book/<int:book_id>',
         views.barrow_a_book, name='barrow_a_book'),
    path('barrowed_books', views.barrowed_books, name='barrowed_books'),
    path('barrowed_books/<int:id>',
         views.barrowed_books_post, name='barrowed_books_01'),
    path('logout', views.logout, name='logout'),
]
