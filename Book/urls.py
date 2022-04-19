"""Book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from Book_App.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', homepage, name="home"),
    path('create_book/', create_book, name="create_book"),
    path('show_all_books/', show_all_books, name="show_all_books"),
    path('edit_book/<int:id>', edit_book, name="edit_book"),
    path('delete_book/<int:id>', delete_book, name="delete_book"),
    path('soft_delete/<int:id>', soft_delete, name="soft_delete"),
    path('show_soft_delete/', show_soft_delete, name="show_soft_delete"),
    path('delete_all_book/', delete_all_book, name="delete_all_book"),


]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('__debug__/', include('debug_toolbar.urls')),
]


