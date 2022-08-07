from unicodedata import name
from django.contrib import admin
from django.urls import path,re_path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('post-data/', TodoView.as_view(), name='post data'),
    # re_path(r'^search-data/?search=(?P<text>[-\w]+)$', SearchTodoView.as_view(), name='search data'),
    path('search-data/', SearchTodoView.as_view(), name='search data')
]