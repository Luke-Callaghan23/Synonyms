"""synonyms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


app_name = 'said_synonyms'
from said_synonyms.views import (
    view_syns_view, 
    add_syns_view,
    search_singles_view,
    search_combinations_view,
    add_view,
    remove_view
)

urlpatterns = [
    path('', view_syns_view, name="Synonyms for 'said'"),
    path('view/', view_syns_view, name="Synonyms for 'said'"),
    path('view/search/singles/', search_singles_view, name="Synonyms for 'said'"),
    path('view/search/combinations/', search_combinations_view, name="Synonyms for 'said'"),
    path('add/', add_syns_view, name="Add Synonyms"),
    path('add/add/', add_view, name="Add Synonyms"),
    path('add/remove/', remove_view, name="Add Synonyms"),
]
