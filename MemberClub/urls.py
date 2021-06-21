from django.urls import path

from . import views

urlpatterns = [
    path('', views.show_members_list, name='all_members'),
    path('new_member', views.new_member, name='new_member'),
]