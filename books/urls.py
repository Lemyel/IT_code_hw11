from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.IndexTemplate.as_view(), name='index'),
    path('about_site', views.AboutList.as_view()),
    path('about_author/<int:pk>', views.AuthorDetail.as_view()),
    path('book/<int:pk>', views.BookDetail.as_view(), name='book'),
    path('add_book/', views.BookAdd.as_view(), name='add_book'),
    path('update_book/<int:pk>', views.BookUpdate.as_view(),
        name='update_book'),
    path('delete_book/<int:pk>', views.BookDelete.as_view(),
        name='delete_book'),
]
