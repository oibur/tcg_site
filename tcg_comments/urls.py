"""Defines URL patterns for tcg_comments"""

from django.urls import path

from . import views

app_name = 'tcg_comments'
urlpatterns = [
    #Comments Page
    path('comments/', views.comments, name='comments'),
    #Page for adding a new comment
    path('new_comment', views.new_comment, name='new_comment'),
]