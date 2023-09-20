
from portfo import views
from django.contrib import admin

from django.urls import path

urlpatterns = [
	
    path('^$'  , views.firstpage, name='firstpage'),
    path('form/'  , views.contact_me, name='contact_me'),
    path('mywork/'  , views.mywork, name='mywork'),
    path('mywork1/'  , views.mywork1, name='mywork1'),

    path('aboutus/'  , views.aboutus, name='aboutus'),
    # pat('', views.PostList.as_view(), name='home'),
    path('frontpage/', views.frontpage, name='frontpage'),
    path('admin/',  admin.site.urls),
    path('<slug:slug>/', views.post_Detail, name='post_Detail'),
    path('index/'  , views.index, name='index'),


]