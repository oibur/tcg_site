"""Defines URL patterns for tcg_cards"""

from django.urls import path

from . import views

app_name = 'tcg_cards'
urlpatterns = [
    #Home Page
    path('', views.index, name='index'),
    path('overview/', views.overview, name='overview'),
    path('totals/', views.totals, name='totals'), 
    path('gen1/', views.gen1, name='gen1'),
    path('gen2/', views.gen2, name='gen2'),
    path('gen3/', views.gen3, name='gen3'),
    path('gen4/', views.gen4, name='gen4'),
    path('gen5/', views.gen5, name='gen5'),
    path('gen6/', views.gen6, name='gen6'),
    path('gen7/', views.gen7, name='gen7'),
    path('gen8/', views.gen8, name='gen8'),
]