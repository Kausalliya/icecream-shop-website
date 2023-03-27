from .import views
from django.urls import path,include

urlpatterns = [

    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('menu',views.menu,name='menu'),
    path('contact',views.contact,name='contact'),

]
