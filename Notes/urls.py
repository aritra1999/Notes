
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView

from notes.views import login_view, list_view, edit_view, search_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name="login"),
    path('login/', login_view, name="login"),
    path('list/', list_view, name="list"),
    path('edit/', edit_view, name="edit"),
    path('search/', search_view, name="search" ),
    path('logout/', LogoutView.as_view(), name="logout")
]
