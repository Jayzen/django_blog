from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("articles/", views.articles, name="articles"),
    path("articles/<int:pk>", views.article, name="article"),
    path("article/<int:pk>/delete/", views.article_delete, name="article_delete"),
    path("articles/new", views.article_new, name="article_new"),
    path("articles/<int:pk>/edit/", views.article_edit, name="article_edit"),
    path('sign-up/', views.sign_up, name='sign_up'),
]